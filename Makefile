.PHONY: build up down logs restart manual-session manual-session-logs

build:
	docker compose build

up:
	docker compose up --build

down:
	docker compose down

logs:
	docker compose logs -f

restart:
	docker compose down
	docker compose up

manual-session:
	docker compose up manual-session --build

manual-session-logs:
	docker compose logs -f manual-session
