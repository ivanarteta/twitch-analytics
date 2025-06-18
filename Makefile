# Variables configurables
APP_NAME = twitch-analytics
PORT = 8000

# Crear entorno virtual (opcional si usas Docker)
.PHONY: venv
venv:
	python -m venv venv && . venv/bin/activate && pip install -r requirements.txt

# Instalar dependencias
.PHONY: install
install:
	pip install -r requirements.txt

# Ejecutar FastAPI en desarrollo
.PHONY: run
run:
	uvicorn app.main:app --reload --host 0.0.0.0 --port $(PORT)

# Ejecutar tests con pytest
.PHONY: test
test:
	pytest

# Formatear código con black
.PHONY: format
format:
	black .

# Linting con flake8 (requiere que lo añadas a requirements.txt)
.PHONY: lint
lint:
	flake8 .

# Build de Docker
.PHONY: build
build:
	docker build -t $(APP_NAME) .

# Correr Docker en modo interactivo
.PHONY: docker-run
docker-run:
	docker run -p $(PORT):8000 $(APP_NAME)

# Limpiar contenedores/imágenes (aviso: destructivo)
.PHONY: clean
clean:
	docker system prune -af

# Levantar contenedores con Docker Compose
.PHONY: dcup
dcup:
	docker-compose up -d

# Parar los contenedores
.PHONY: dcdown
dcdown:
	docker-compose down

# Ver logs de los contenedores
.PHONY: dclogs
dclogs:
	docker-compose logs -f

# Reconstruir los contenedores con cambios
.PHONY: dcbuild
dcbuild:
	docker-compose up --build -d	

# Ayuda
.PHONY: help
help:
	@echo "Comandos disponibles:"
	@echo "  make install      -> Instala dependencias"
	@echo "  make run          -> Ejecuta FastAPI localmente"
	@echo "  make test         -> Ejecuta los tests"
	@echo "  make format       -> Formatea el código"
	@echo "  make lint         -> Linter con flake8"
	@echo "  make build        -> Build Docker sin Compose"
	@echo "  make dcup         -> docker-compose up -d"
	@echo "  make dclogs       -> Ver logs de docker-compose"
	@echo "  make dcdown       -> docker-compose down"
	@echo "  make dcbuild      -> docker-compose up --build -d"
	@echo "  make clean        -> Elimina imágenes/volúmenes no usados"
