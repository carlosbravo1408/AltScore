from flask import Blueprint

api = Blueprint('drifting_ship_api', __name__, url_prefix='/')
SYSTEMS = {
  "navigation": "NAV-01",
  "communications": "COM-02",
  "life_support": "LIFE-03",
  "engines": "ENG-04",
  "deflector_shield": "SHLD-05"
}
damaged_system = "life_support"


@api.route('/status', methods=['GET'])
def status():
    return {
        "damaged_system": damaged_system
    }


@api.route('/repair-bay', methods=['GET'])
def repair_bay():
    anchor_code = SYSTEMS.get(damaged_system, "UNKNOWN")
    html = f"""
    <!DOCTYPE html>
    <html>
    <head>
       <title>Repair</title>
    </head>
    <body>
    <div class=\"anchor-point\">{anchor_code}</div>
    </body>
    </html>
    """
    return html, 200, {'Content-Type': 'text/html'}


@api.route('/teapot', methods=['POST'])
def teapot():
    return {'message': "I'm a teapot"}, 418
