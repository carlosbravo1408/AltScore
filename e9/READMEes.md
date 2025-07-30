# Nave a la Deriva API 🚀 Sistema de Reparación de Emergencia - Parte 2

## Descripción General

> Te encuentras atrapado en una nave espacial a la deriva en el espacio profundo. Los sistemas de navegación están dañados y la energía se agota rápidamente. En un golpe de suerte, detectas en el radar un robot de reparación no tripulado que se aproxima. Sabes que este robot utiliza llamadas HTTP para identificar y reparar sistemas averiados en naves cercanas. Tu única esperanza es simular una llamada de auxilio para que el robot te encuentre y repare tu nave.

## Requerimientos:

Crea tu entorno virtual y en este instala las dependencias de `requirements.txt`

```bash
python3 -m venv .venv
source ./.venv/bin/activate
pip install -r requirements.txt
```

## ## Uso

1. Arrancar la API:

```bash
python ./e7_api.py
```

2. La API estará disponible en `http://localhost:5000`
3. Para exponer públicamente se sugiere usar [ngrok](https://ngrok.com/)

```bash
ngrok http 5000 # O el puerto que hayas elegido
```

4. Obtener la ruta que direccional a tu API local:

```bash
Forwarding                    https://someHexId.ngrok-free.app -> http://localhost:5000  
```

## API Endpoints

### 1. GET /status

Retorna la información del sistema dañado.

**Response:**

```json
{
  "damaged_system": "communications"
}
```

### 2. GET /repair-bay

Retorna la pagina HTML con el *anchor point* para reparar el robot.

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

Retorna el código de estado HTTP 418  (I'm a teapot).

**Response:**

```html
HTTP/1.1 418 I'M A TEAPOT
```

### 4. GET /phase-change-diagram

Retorna el volumen especifico para el fluido según el diagrama de cambio de fase propuesto (Phase 2).

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