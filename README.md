# 🎮 Twitch Analytics API

Esta aplicación permite consultar datos de usuarios y streams en vivo desde la API pública de Twitch, gestionando la autenticación OAuth automáticamente.

---

## 🚀 Tecnologías utilizadas

- [FastAPI](https://fastapi.tiangolo.com/) – Framework web moderno en Python
- [Uvicorn](https://www.uvicorn.org/) – Servidor ASGI para FastAPI
- [Docker](https://www.docker.com/) y [Docker Compose](https://docs.docker.com/compose/)
- [httpx](https://www.python-httpx.org/) – Cliente HTTP asíncrono
- [pytest](https://docs.pytest.org/) – Framework de testing
- [dotenv](https://pypi.org/project/python-dotenv/) – Carga de variables de entorno

---

## ⚙️ Endpoints

### `/analytics/user?id=<twitch_user_id>`

- Devuelve la información de un usuario de Twitch por su ID.
- Requiere el parámetro `id`.
- Gestiona expiración de tokens y errores comunes.

### `/analytics/streams`

- Devuelve una lista de streams actualmente en vivo.
- Utiliza el token OAuth automáticamente.


## 📌 Decisiones técnicas

- Elijo Python como lenguaje para explorar nuevos lenguajes de desarrollo y por su capacidad para poder ser montado en docker fácilmente.
- Se elige FastAPI por su claridad, rendimiento y facilidad para montar una API REST rápidamente.
- Uso de httpx para llamadas a API externa.