from flask import Flask
from flask_cors import CORS

from e7.web.views import api
from lib.constants import Constants


app = Flask("DriftingShip")
CORS(app)


def register_blueprints():
    app.register_blueprint(api.drifting_ship_api)


if __name__ == '__main__':
    print("Starting DriftingShip API V1.0...")
    print(f"API will be available on port {Constants.get('PORT', 5000)}...")
    print("Endpoints:")
    print(f"   GET  /status                - Returns damaged system info")
    print(f"   GET  /repair-bay            - Returns HTML with anchor point")
    print(f"   POST /teapot                - Returns HTTP 418 status")
    register_blueprints()
    app.run(debug=False, host='0.0.0.0', port=Constants.get("PORT", 5000))
