from lib.altscoreapi_helper import AltScoreApiHelper
from lib.constants import Constants
from lib.swapi_helper import SWApiHelper


if __name__ == "__main__":
    token = Constants.API_KEY
    api = AltScoreApiHelper(token)
    swapi = SWApiHelper()

    # Get All Star Wars people and make all predictions
    sw_people = swapi.get_people()
    api.s1_e3_get_oracle_rolodex_prediction(sw_people)

    planets = dict()
    dark_side = 0
    light_side = 0
    people_count = 0
    for data in sw_people.values():
        planet = data["planet"]
        if planet not in planets:
            planets[planet] = {
                "Light Side": 0,
                "Dark Side": 0,
                "People Count": 0
            }
        planets[planet]["People Count"] += 1
        if "Light Side" in data["prediction"]:
            planets[planet]["Light Side"] += 1

        if "Dark Side" in data["prediction"]:
            planets[planet]["Dark Side"] += 1

    for planet_name, data in planets.items():
        if data["Light Side"] == data["Dark Side"]:
            if api.s1_e3_send_solution(planet_name):
                print("Success!")
            else:
                print("Failure!")
            break