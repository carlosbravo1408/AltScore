from flask import Flask
from flask_cors import CORS

from e7.web.views import api as e7_api
from e9.web.views import api as e9_api
from lib.constants import Constants


app = Flask("DriftingShip")
CORS(app)


def register_blueprints():
    app.register_blueprint(e7_api.drifting_ship_api)
    app.register_blueprint(e9_api.drifting_ship_part2_api)


if __name__ == '__main__':
    register_blueprints()
    print("Starting DriftingShip API V1.1...")
    print(f"API will be available on port {Constants.get('PORT', 5000)}...")
    print("Endpoints:")
    print(f"   GET  /status                - Returns damaged system info")
    print(f"   GET  /repair-bay            - Returns HTML with anchor point")
    print(f"   POST /teapot                - Returns HTTP 418 status")
    print(f"   GET  /phase-change-diagram  - Returns P-v diagram data")
    app.run(debug=False, host='0.0.0.0', port=Constants.get("PORT", 5000))