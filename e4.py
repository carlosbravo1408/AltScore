from lib.altscoreapi_helper import AltScoreApiHelper
from lib.constants import Constants


if __name__ == "__main__":
    token = Constants.API_KEY
    api = AltScoreApiHelper(token)
    user, password = api.s1_e4_get_user_and_password()
    # username: "Not all those who wander"
    # password: "are lost"
    if api.s1_e4_send_solution(user, password):
        print("Success!")
    else:
        print("Fail!")
