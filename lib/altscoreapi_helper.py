import json
import math
from base64 import b64decode
from typing import Dict, List, Any, Tuple, Union, Optional

import requests
from bs4 import BeautifulSoup
from requests import Response


class AltScoreApiHelper:
    API_URL = "https://makers-challenge.altscore.ai/v1/"
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.__headers = {"Api-Key": self.api_key}

    @classmethod
    def register(
            cls,
            alias: str,
            country: str,
            email: str,
            apply_role: str
    ) -> Dict[str, str]:
        payload = {
            "alias": alias,
            "country": country,
            "email": email,
            "apply_role": apply_role
        }
        response = requests.post(
            url=f"{cls.API_URL}register",
            json=payload
        )
        response.raise_for_status()
        return response.json()

    def s1_e1_get_measurement(self) -> Dict[str, str]:
        response = requests.get(
            url=f"{self.API_URL}s1/e1/resources/measurement",
            headers=self.__headers
        )
        response.raise_for_status()
        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(response.json())

    def s1_e1_send_solution(self, speed: int) -> bool:
        payload = {"speed": speed}
        response = requests.post(
            url=f"{self.API_URL}s1/e1/solution",
            json=payload,
            headers=self.__headers
        )
        response.raise_for_status()
        if response.status_code == 200:
            return response.json().get("result", "") ==  "correct"
        else:
            raise Exception(response.json())

    def s1_e2_get_stars_by_page(
            self,
            sort_by: str = "id",
            sort_direction: str = "desc",
            page_number: int = 1,
    ) -> Response:
        uri = (
            f"{self.API_URL}s1/e2/resources/stars?sort-by={sort_by}&"
            f"sort-direction={sort_direction}&"
            f"page={page_number}"
        )
        return requests.get(
            url=uri,
            headers=self.__headers
        )

    def s1_e2_get_stars(
            self,
            sort_by: str = "id",
            sort_direction: str = "desc"
    ) -> List[Dict[str, Union[str, float, int]]]:
        data = []
        page_number = 1
        total_stars = 1e3 # Unknown until the first GET request
        stars_per_page = 1
        total_pages = int(math.ceil(total_stars / stars_per_page))
        while page_number <= total_pages:
            response = self.s1_e2_get_stars_by_page(
                sort_by, sort_direction, page_number)
            page_number += 1
            response.raise_for_status()
            total_stars = int(response.headers.get("x-total-count", 1e3))
            if response.status_code == 200:
                if len(list(response.json())) > 0:
                    data.extend(response.json())
                    if len(list(response.json())) > stars_per_page:
                        stars_per_page = len(response.json())
                        total_pages = math.ceil(total_stars / stars_per_page)
                else:
                    break
            else:
                raise Exception(response.json())
        return data

    def s1_e2_send_solution(self, average_resonance: int) -> bool:
        payload = {"average_resonance": average_resonance}
        response = requests.post(
            url=f"{self.API_URL}s1/e2/solution",
            json=payload,
            headers=self.__headers
        )
        response.raise_for_status()
        if response.status_code == 200:
            return response.json().get("result", "") ==  "correct"
        else:
            raise Exception(response.json())

    def s1_e3_get_oracle_rolodex_prediction(
            self,
            sw_people: Dict[str, Dict[str, str]]
    ) -> None:
        url = self.API_URL + "s1/e3/resources/oracle-rolodex?name={name}"
        for name in sw_people:
            response = requests.get(
                url=url.format(name=name),
                headers=self.__headers
            )
            response.raise_for_status()
            if response.status_code == 200:
                sw_people[name]["prediction"] = str(
                    b64decode(response.json().get("oracle_notes"))
                )

    def s1_e3_send_solution(self, planet_name: str) -> bool:
        payload = {"planet": planet_name}
        response = requests.post(
            url=f"{self.API_URL}s1/e3/solution",
            headers=self.__headers,
            json=payload
        )
        response.raise_for_status()
        if response.status_code == 200:
            return response.json().get("result", "") ==  "correct"
        else:
            raise Exception(response.json())

    def s1_e4_get_user_and_password(
            self
    ) -> Tuple[Optional[str], Optional[str]]:
        url = "https://makers-challenge.altscore.ai/s1e4"
        response = requests.get(url)
        html = response.text
        soup = BeautifulSoup(html, "html.parser")
        user_p_element = None
        password_p_element = None
        for p_element in soup.find_all("p"):
            if "Usuario: ???" in p_element.get_text():
                user_p_element = p_element
            if "Contraseña: " in p_element.get_text():
                password_p_element = p_element
            if user_p_element is not None and password_p_element is not None:
                break
        user = user_p_element.find("span").text.strip() \
            if user_p_element else None
        password = password_p_element.find("input")["value"].strip() \
            if password_p_element else None
        return user, password

    def s1_e4_send_solution(self, username: str, password: str) -> bool:
        payload = {"username": username, "password":password}
        response = requests.post(
            url=f"{self.API_URL}s1/e4/solution",
            headers=self.__headers,
            json=payload
        )
        response.raise_for_status()
        if response.status_code == 200:
            return response.json().get("result", "") ==  "correct"
        else:
            raise Exception(response.json())

    def s1_e5_start_challenge(self) -> bool:
        response = requests.post(
            url=f"{self.API_URL}s1/e5/actions/start",
            headers=self.__headers
        )
        response.raise_for_status()
        return response.status_code == 200

    def s1_e5_get_radar_read(self) -> Tuple[str, str, str]:
        payload = {
            "action": "radar",
            "attack_position": None
        }
        response = requests.post(
            url=f"{self.API_URL}s1/e5/actions/perform-turn",
            headers=self.__headers,
            json=payload
        )
        response.raise_for_status()
        if response.status_code == 200:
            turns_remaining = response.json().get("turns_remaining", "")
            timing_remaining = response.json().get("time_remaining", "")
            message = response.json().get("message", "")
            return turns_remaining, timing_remaining, message
        raise Exception(response.json())

    def s1_e5_send_enemy_prediction(
            self,
            enemy_position: Dict[str, Union[str, int]]
    ) -> bool:
        payload = {
            "action": "attack",
            "attack_position": enemy_position
        }
        response = requests.post(
            url=f"{self.API_URL}s1/e5/actions/perform-turn",
            headers=self.__headers,
            json=payload
        )
        response.raise_for_status()
        if response.status_code == 200:
            attack_result = response.json().get("action_result", "").lower()
            if attack_result:
                if (
                    "destroyed" in attack_result or
                    "hit" in attack_result or
                    "eliminated" in attack_result
                ):
                    return True
            return False
        raise Exception(response.json())

    def s1_e6_send_solution(self, pokemon_heights: Dict[str, float]) -> bool:
        payload = {
            "heights": json.loads(json.dumps(pokemon_heights, sort_keys=True))
        }
        response = requests.post(
            url=f"{self.API_URL}s1/e6/solution",
            headers=self.__headers,
            json=payload
        )
        response.raise_for_status()
        if response.status_code == 200:
            return response.json().get("result", "") == "correct"
        else:
            raise Exception(response.json())

    def s1_e8_door_action(
            self,
            cookie: Optional[Dict[str, str]] = None
    ) -> Tuple[bool, Optional[str]]:
        response = requests.post(
            url=f"{self.API_URL}s1/e8/actions/door",
            headers=self.__headers,
            cookies=cookie
        )
        if response.status_code == 403:
            return False, None
        if response.status_code == 200:
            cookie = response.headers.get("Set-Cookie")
            message = None
            if cookie is not None:
                if "gryffindor" in cookie:
                    message = cookie.split(";")[0].replace("gryffindor=", "")
            return True, message
        return False, None

    def s1_e8_send_solution(self, secret_message: str) -> bool:
        payload = {
            "hidden_message": secret_message
        }
        response = requests.post(
            url=f"{self.API_URL}s1/e8/solution",
            headers=self.__headers,
            json=payload
        )
        response.raise_for_status()
        if response.status_code == 200:
            return response.json().get("result", "") == "correct"
        else:
            raise Exception(response.json())
