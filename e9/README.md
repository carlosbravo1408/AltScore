# Drifting Spaceship API 🚀 Emergency Repair System - Part 2

## Overview

> You are stranded aboard a drifting spaceship in deep space. The navigation systems are damaged, and the power is rapidly running out. By a stroke of luck, you detect an unmanned repair robot approaching on the radar. You know this robot uses HTTP requests to identify and fix damaged systems on nearby ships. Your only hope is to simulate a distress call so the robot can find and repair your ship.

## Requirements:

Create a virtual environment and install the dependencies from `requirements.txt`:

```bash
python3 -m venv .venv
source ./.venv/bin/activate
pip install -r requirements.txt
```

## Usage

1. Start the API:

```bash
python ./e7_api.py
```

1. The API will be available at `http://localhost:5000`
2. To expose it publicly, [ngrok](https://ngrok.com/) is recommended:

```bash
ngrok http 5000 # Or the port you've chosen
```

1. Get the forwarding URL that points to your local API:

```bash
Forwarding                    https://someHexId.ngrok-free.app -> http://localhost:5000  
```

## API Endpoints

### 1. GET /status

Returns the damaged system information.

**Response:**

```json
{
  "damaged_system": "communications"
}
```

### 2. GET /repair-bay

Returns an HTML page with an anchor point for the repair robot.

**Response:**

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Repair</title>
  </head>
  <body>
    <div class="anchor-point">COM-02</div>
  </body>
</html>
```

### 3. POST /teapot

Returns HTTP 418 status code (I'm a teapot).

**Response:**

```html
HTTP/1.1 418 I'M A TEAPOT
```

### 4. GET /phase-change-diagram

Returns specific volume data for hydraulic fluid phase change (Phase 2).

**Parameters:**

- `pressure` (float): Pressure in MPa

**Example:**

```
GET /phase-change-diagram?pressure=10
```

**Response:**

```
{
  "specific_volume_liquid": 0.0035,
  "specific_volume_vapor": 0.0035
}
```