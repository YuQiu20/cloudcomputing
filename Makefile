Definieer de targets die uitgevoerd kunnen worden
.PHONY: deploy build down restart logs

Variabele voor het Docker Compose bestand
COMPOSE_FILE = docker-compose.yml

De 'deploy' target roept achtereenvolgens 'build', 'down' en 'up' aan.
Dit simuleert de automatische update: nieuwe code -> nieuwe image -> nieuwe stack.
deploy: build down up

Stap 1: Bouwen van de containers. --no-cache is cruciaal voor nieuwe code.
build:
@echo "Stap 1: Containers bouwen (build)..."
docker compose -f $(COMPOSE_FILE) build --no-cache

Stap 2: Stoppen en verwijderen van oude containers (behoud named volumes).
down:
@echo "Stap 2: Oude containers stoppen (down)..."
docker compose -f $(COMPOSE_FILE) down

Stap 3: Opstarten van de nieuwe stack (-d voor detached mode, --force-recreate).
up:
@echo "Stap 3: Nieuwe stack opstarten..."
docker compose -f $(COMPOSE_FILE) up -d --force-recreate

Standaard restart (down dan up) ZONDER nieuwe build.
restart: down up

Toon de logs van de draaiende containers
logs:
docker compose logs -f
