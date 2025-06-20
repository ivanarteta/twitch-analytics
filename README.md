# 🎮 Twitch Analytics API

Esta aplicación permite consultar datos de usuarios y streams en vivo desde la API pública de Twitch, gestionando la autenticación OAuth automáticamente.

---

## 🚀 Tecnologías utilizadas

- [FastAPI](https://fastapi.tiangolo.com/) – Framework web moderno en Python
- [Uvicorn](https://www.uvicorn.org/) – Servidor ASGI para FastAPI
- [Docker](https://www.docker.com/) y [Docker Compose](https://docs.docker.com/compose/)
- [httpx](https://www.python-httpx.org/) – Cliente HTTP asíncrono
- [dotenv](https://pypi.org/project/python-dotenv/) – Carga de variables de entorno

---

## 🧰 Requisitos previos

- Tener Docker y Docker Compose instalados (recomendado: Docker Desktop).
- En Windows, usar Git Bash o WSL si se desea trabajar con `make`.
- Tener un archivo `.env` con las siguientes claves: TWITCH_CLIENT_ID=tu_client_id y TWITCH_CLIENT_SECRET=tu_client_secret

## Ejecución de la aplicación

- Crear un .env con las variables TWITCH_CLIENT_ID y TWITCH_CLIENT_SECRET para acceder a la API externa de Twitch
- En la raíz del proyecto, ejecutar make dcup, en caso de no tener make, ejecutar docker compose up -d
- Una vez se hace la build del contenedor (solo la primera vez) y se levanta, acceder en el navegador a localhost:8000/docs para acceder a la documentación de la API
- Probar los endpoints.

## ⚙️ Endpoints

### `/analytics/user?id=<twitch_user_id>`

- Devuelve la información de un usuario de Twitch por su ID.
- Requiere el parámetro `id`.
- Ids de ejemplo: SirMaza -> 39518378 y AuronPlay -> 459331509

### `/analytics/streams`

- Devuelve una lista de streams actualmente en vivo.


## 📌 Decisiones técnicas

- Elijo Python como lenguaje para explorar nuevos lenguajes de desarrollo y por su capacidad para poder ser montado en docker fácilmente.
- Se elige FastAPI por su claridad, rendimiento y facilidad para montar una API REST rápidamente.
- Uso de httpx para llamadas a API externa.

## 🧠 Proceso de desarrollo

- Lectura de requerimientos y selección del lenguaje y tecnologías a utilizar
- Montaje del esqueleto del proyecto y arquitectura Docker
- Lectura de la documentación de la API de twitch para saber sus estructuras de respuesta y peticiones
- Desarrollo de la petición para obtener el token de twitch para posteriores peticiones
- Desarrollo del endpoint para recoger datos de un usuario de twitch por id con manejo de errores
- Desarrollo del endpoint para recoger datos de los directos en ese momento con manejo de errores
- Desarrollo del regenerar token en el caso de que la perimera vez sea inválido y refactorización del código