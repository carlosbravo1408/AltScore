# AltScore Challenge

This repository contains my solutions to the AltScore Season 1 challenges. All implementations were done in Python 3.10, so feel free to review any file.

You’ll need a `.env` file containing the token assigned to you upon registration (it also includes the port for exposing the Flask services used in challenges 7 and 9):

```bash
API_KEY=AnyAPIKey
PORT=5000 #Optional
```

## Requirements

Create a virtual environment and install the dependencies from `requirements.txt`:

```bash
python3 -m venv .venv
source ./.venv/bin/activate
pip install -r requirements.txt
```

## Registration

You can register via the [documentation page](https://makers-challenge.altscore.ai/docs#/Register/handler_v1_register_post), or directly using `AltScoreApiHelper`:

```python
from lib.altscoreapi_helper import AltScoreApiHelper

AltScoreApiHelper.register(
    alias= "GreatAlias0074",
    country= "ECU",
    email= "any_email@awesomemail.com",
    apply_role= "engineering"
)
```

If everything goes well, you should receive a response like this:

```json
{
  "message": "API-KEY generated and sent to your email, check the notifications folder"
}
```

## My Solutions

### E1 [The Silent Probe](https://makers-challenge.altscore.ai/s1e1): 100 Points

[./e1.py](./e1.py)

### E2 [The Cosmic Enigma of Kepler-452b](https://makers-challenge.altscore.ai/s1e2): 100 Points

[./e2.py](./e2.py)

In this challenge I propose two possible solutions. The most optimal (in my opinion) involves requesting only the first 3 stars once, sorted in ascending order by resonance. The pattern is visible, so requesting the remaining 97 stars may be unnecessary.

### E3 [The Search for the Lost Sith Temple](https://makers-challenge.altscore.ai/s1e3): 100 Points

[./e3.py](./e3.py)

As Freddie Mercury would say: "[And I don't like *Star Wars*](https://genius.com/1232653/Queen-bicycle-race/You-say-shark-i-say-hey-man-jaws-was-never-my-scene-and-i-dont-like-star-wars)" XD

### E4 [The Quest for the Forgotten Elven Forge](https://makers-challenge.altscore.ai/s1e4): 100 Points

[./e4.py](./e4.py)

The highlight of this challenge was using BeautifulSoup to extract the hidden username and password from the HTML content.

### E5 [The Final Stand of the "Valiant" - Countdown!](https://makers-challenge.altscore.ai/s1e5): 300 Points (You need at least 300 points to unlock this challenge)

[./e5.ipynb](./e5.ipynb)

I implemented this one in a Jupyter Notebook for easier visualization. The enemy ship’s movement resembles that of a knight on a chessboard.

### E6 [Infiltration into Prism City](https://makers-challenge.altscore.ai/s1e6): 100 Points

[./e6.py](./e6.py)

Gotta catch 'em all! I used threading to make multiple requests in parallel.

### E7 [Drifting Ship](https://makers-challenge.altscore.ai/s1e7): 150 Points

[./e7/](./e7/README.md)

To run the Flask service for this challenge, execute `./e7/e7_api.py`.

### E8 [The Spell of the Magic Gate](https://makers-challenge.altscore.ai/s1e8): 150 Points

[./e8.py](./e8.py)

If you know the value of the first cookie, the rest is a piece of cake. As a tip, send your POST request when the clock shows zero seconds.

### E9: [Drifting Ship - Part 2](https://makers-challenge.altscore.ai/s1e9): 300 Points

[./e9/](./e9/README.md)

To run the Flask service for this challenge, execute `./e9/e9_api.py`.

### E10 [Uncovering the Cost of Living in the Galactic Empire](https://makers-challenge.altscore.ai/s1e10): 500 Points (Coming Soon)

...

### E11 [Final Boss](https://www.youtube.com/watch?v=dQw4w9WgXcQ): 1000 Points

I got *Rickrolled*. I was way too naive clicking a link with the legendary `dQw4w9WgXcQ`. I probably deserved the 1000 points just for getting trolled XD