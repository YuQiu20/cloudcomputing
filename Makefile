.PHONY: up down restart logs

up:
docker compose up -d

down:
docker compose down

restart:
docker compose down && sleep 2 && docker compose up -d

logs:
docker compose logs -f
