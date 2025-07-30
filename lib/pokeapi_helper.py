from typing import Dict, Any, Union, List

import requests


class PokeApiHelper:

    @classmethod
    def get_pokemon_types(cls) -> Dict[str, Any]:
        types = {
            _type["name"]: []
            for _type in requests.get(
                "https://pokeapi.co/api/v2/type/?offset=0&limit=100"
            ).json().get("results")
        }
        return types

    @classmethod
    def get_pokemon_data(
            cls,
            pokemon_url: str
    ) -> Dict[str, Union[List[str], float, str]]:
        response = requests.get(pokemon_url)
        response.raise_for_status()
        pokemon_data = response.json()
        output_data = {
            "types": [_type["type"]["name"] for _type in pokemon_data["types"]],
            "height": pokemon_data["height"],
        }
        return output_data

    @classmethod
    def get_pokemons_from_offset_limit(
            cls,
            pokemon_collection: Dict[str, Any],
            offset: int,
            limit: int = 100
    ) -> None:
        url = f"https://pokeapi.co/api/v2/pokemon/?offset={offset}&limit={limit}"
        response = requests.get(url)
        response.raise_for_status()
        for pokemon in response.json()["results"]:
            pokemon_collection[pokemon["name"]] = cls.get_pokemon_data(
                pokemon["url"])
