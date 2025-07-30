from lib.altscoreapi_helper import AltScoreApiHelper
from lib.constants import Constants


if __name__ == "__main__":
    token = Constants.API_KEY
    api = AltScoreApiHelper(token)

    # Option 1: fetch All starts and get resonance Average
    # The order is trivial if you are going to get all the stars in the end.
    stars = api.s1_e2_get_stars()
    counter = 0
    resonance_avg = round(sum([s["resonance"] for s in stars]) / len(stars))
    if api.s1_e2_send_solution(resonance_avg):
        print("Success")
    else:
        print("Failed")

    # Option 2: Getting the first (maybe second) batch of stars, you can see
    # a pattern if the stars are ordered ascendingly that has steps of 7,
    # starting at 42, ending at 735
    response = api.s1_e2_get_stars_by_page(
        sort_by="resonance", sort_direction="asc", page_number=1
    )
    total_stars = int(response.headers["x-total-count"])
    first_start = list(response.json())[0]
    first_resonance = int(first_start["resonance"])
    common_diff = [
        response.json()[i]["resonance"] - response.json()[i-1]["resonance"]
        for i in range(1, len(response.json()))
    ]
    if all([
        common_diff[i] == common_diff[i+1] for i in range(len(common_diff) - 1)
    ]):
        resonance_step = common_diff[0]
    else:
        raise Exception('Resonances are not an arithmetic sequence')
    # The latest resonance can be found by making a Get request with page
    # number 34 or...
    last_resonance = (total_stars - 1) * resonance_step + first_resonance
    resonance_avg = round(0.5 * (last_resonance + first_resonance))
    if api.s1_e2_send_solution(resonance_avg):
        print("Success")
    else:
        print("Failed")
