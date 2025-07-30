import time
from base64 import b64decode
from datetime import datetime
from lib.altscoreapi_helper import AltScoreApiHelper
from lib.constants import Constants


if __name__ == '__main__':
    token = Constants.API_KEY
    api = AltScoreApiHelper(token)
    cookies = []
    # The first door will open at 0 seconds
    while True:
        if datetime.now().time().second == 0:
            break
        time.sleep(0.5)

    print("It is the right time, the key to the first door will be revealed")

    # But if you don't want to wait, you can use the next first token
    #  {"gryffindor":"QWx0d2FydHM="}

    last_cookie = None
    while True:
        current_state, cookie = api.s1_e8_door_action(last_cookie)
        if cookie is not None:
            cookies.append(cookie)
            last_cookie = {"gryffindor":cookie}
        else:
            break

    print("All the doors have been opened in the correct order")

    secret_message = " ".join([b64decode(cookie).decode() for cookie in cookies])
    print(
        "We apply `Revelio` to the hidden message and the secret has been "
        "revealed:", secret_message
    )

    if api.s1_e8_send_solution(secret_message):
        print("Success")
    else:
        print("Failed")

