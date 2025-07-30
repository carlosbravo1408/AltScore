from threading import Thread

from lib.altscoreapi_helper import AltScoreApiHelper
from lib.pokeapi_helper import PokeApiHelper
from lib.constants import Constants


if __name__ == '__main__':

    token = Constants.API_KEY
    api = AltScoreApiHelper(token)

    pokemon_types = PokeApiHelper.get_pokemon_types()
    sorted_type_keys = sorted([k for k in pokemon_types.keys()])

    # Parallel processing
    limit = 100
    threads = []
    pokemons_collection = dict()
    pokemon_count = 1302

    for i in range(0, pokemon_count+1, limit):
        threads.append(
            Thread(
                target=PokeApiHelper.get_pokemons_from_offset_limit,
                args=(pokemons_collection, i, limit)
            )
        )
        threads[-1].start()

    for thread in threads:
        thread.join()

    for pokemon in pokemons_collection.values():
        for _type in pokemon["types"]:
            pokemon_types[_type].append(pokemon["height"])

    heights = {
        key: round(sum(val) / len(val), 3)
        for key, val in pokemon_types.items() if len(val) > 0
    }

    if api.s1_e6_send_solution(heights):
        print("Success!")
    else:
        print("Fail!")
