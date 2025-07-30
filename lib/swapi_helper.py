from typing import Dict, Any, Optional

import requests


class SWApiHelper:
    @classmethod
    def get_planet_info(cls, planet_url: str) -> Optional[Dict[str, Any]]:
        planet_response = requests.get(
            url=planet_url,
            verify=False
        )
        planet_response.raise_for_status()
        if planet_response.status_code == 200:
            return planet_response.json()
        return None


    @classmethod
    def get_people(cls) -> Dict[str, Dict[str, str]]:
        people = {}
        url = "https://swapi.dev/api/people/?page={page}"
        planets = dict()
        page = 1

        while True:
            response = requests.get(
                url=url.format(page=page),
                verify=False
            )
            if response.status_code == 200:
                for person_data in response.json().get("results", []):
                    planet_url = person_data.get("homeworld")
                    planet_id = planet_url.split("/")[-2]
                    if planet_id not in planets:
                        planet_response = cls.get_planet_info(planet_url)
                        if planet_response is not None:
                            planets[planet_id] = planet_response.get("name")
                    people[person_data.get("name")] = {
                        "planet": planets[planet_id]
                    }
            else:
                break
            page += 1

        return people