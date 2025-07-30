from time import sleep

from lib.altscoreapi_helper import AltScoreApiHelper
from lib.constants import Constants


if __name__ == "__main__":

    token = Constants.API_KEY
    api = AltScoreApiHelper(token)
    distance, time = None, None
    print("Trying to get readings (1s Period)")
    attempts_count = 0
    while distance is None and time is None:
        attempts_count += 1
        measurement = api.s1_e1_get_measurement()
        try:
            distance = float(measurement["distance"].split(" ")[0])
            time = float(measurement["time"].split(" ")[0])
            velocity = round(distance / time)
            print(
                f"In attempt {attempts_count} with distance {distance} and "
                f"time {time} the velocity {velocity} was obtained"
            )
            if api.s1_e1_send_solution(velocity):
                print("Success! :D")
            else:
                print("Failure! :C")
        except ValueError:
            print(f"Attempt '{attempts_count}' without success")
            distance, time = None, None
        sleep(1)

    #solution 405