# Reto AltScore 

En este repositorio esta mis soluciones a los retos de AltScore Season 1. Toda implementacion la hice en Python3.10, por lo que puedes sentirte libre de revisar cualquier archivo.

Es necesario tener un archivo `.env` con el token que te asignaron al registrarte (tambien contiene el puerto al cual deseas exponer los servicios de Flask de los problemas 7 y 9):

```bash
API_KEY=AnyAPIKey
PORT=5000 #Optional
```

## Requerimientos:

Crea tu entorno virtual y en este instala las dependencias de `requirements.txt`

```bash
python3 -m venv .venv
source ./.venv/bin/activate
pip install -r requirements.txt
```

## Registro

Puedes hacerlo desde la pagina de [documentacion](https://makers-challenge.altscore.ai/docs#/Register/handler_v1_register_post), o desde `AltScoreApiHelper`:

```python
from lib.altscoreapi_helper import AltScoreApiHelper

AltScoreApiHelper.register(
    alias= "GreatAlias0074",
    country= "ECU",
    email= "any_email@awesomemail.com",
    apply_role= "engineering"
)
```

Si todo ha ido bien, deberias tener un mensaje de respuesta como este

```json
{
  "message": "API-KEY generated and sent to your email, check the notifications folder"
}
```



## Mis Soluciones 

### E1 [La Sonda Silenciosa](https://makers-challenge.altscore.ai/s1e1): 100 Puntos:

[./e1.py](./e1.py)

### E2 [El Enigma Cósmico de Kepler-452b](https://makers-challenge.altscore.ai/s1e2) 100 Puntos:

[./e2.py](./e2.py)

En este ejercicio propongo dos posibles soluciones, la mas optima (creo) es unicamente solicitando una única vez las primeras 3 estrellas, en orden ascendente ordenadas por resonancia. El patrón es visible, por lo que hacer las solicitudes a las 97 estrellas restantes quizá están de mas.

### E3 [La Búsqueda del Templo Sith Perdido](https://makers-challenge.altscore.ai/s1e3): 100 Puntos:

[./e3.py](./e3.py)

Como diría Freddy Mercury: "[And I don't like *Star Wars*](https://genius.com/1232653/Queen-bicycle-race/You-say-shark-i-say-hey-man-jaws-was-never-my-scene-and-i-dont-like-star-wars)" XD

### E4 [La Búsqueda de la Forja Élfica Olvidada](https://makers-challenge.altscore.ai/s1e4): 100 Puntos

[./e4.py](./e4.py)

La novedad en este ejercicio o problema es que use BeautyfulSoup para obtener el usuario y la contraseña ocultas en el contenido HTML.

### E5 [La Última Defensa de la "Valiant" - ¡Cuenta Regresiva!](https://makers-challenge.altscore.ai/s1e5): 300 Puntos, y requieres mínimo 300 Puntos para acceder a este reto

[./e5.ipnby](./e5.ipynb)

Aquí lo hice en un JupyterNotebook para facilitarme la visualización, los pasos que da la nave enemiga se asemejan a los movimientos que hace la pieza de ajedrez del caballo en el tablero.

### E6 [La Infiltración en Ciudad Prisma](https://makers-challenge.altscore.ai/s1e6): 100 Puntos

[./e6.py](./e6.py)

Tengo que atraparlos.! Aproximación con Threads para hacer unas cuantas solicitudes en paralelo

### E7 [Nave a la deriva](https://makers-challenge.altscore.ai/s1e7): Puntos 150

[./e7/](./e7/READMEes.md)

Para correr el servicio Flask de este problema, debes ejecutar `./e7/e7_api.py`

### E8 [El Hechizo de La puerta mágica](https://makers-challenge.altscore.ai/s1e8): 150 Puntos

[./e8.py](./e8.py)

Si conoces el valor de la primera Cookie, lo restante es pan comido. Como sugerencia, has tu solicitud POST cuando el reloj marque alguna hora con el segundero en cero

### E9: [Nave a la deriva - Parte 2](https://makers-challenge.altscore.ai/s1e9): Puntos 300

[./e9/](./e9/READMEes.md)

Para correr el servicio Flask de este problema, debes ejecutar `./e9/e9_api.py`

### E10 [Uncovering the Cost of Living in the Galactic Empire](https://makers-challenge.altscore.ai/s1e10): 500 Puntos (Próximamente)

...

### E11 [Final Boss](https://www.youtube.com/watch?v=dQw4w9WgXcQ): 1000 puntos

He sido *Rickrolleado*, he sido muy ingenuo al acceder a la URL conociendo la mítica `dQw4w9WgXcQ`. Debí merecer los 1000 puntos por dejarme `trollear` XD

