.PHONY: build up down logs restart manual-session manual-session-logs build-persistent run-persistent persistent-logs

build:
	docker compose build

up:
	docker compose up adk --build

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

build-persistent:
	docker compose build persistent-session

run-persistent:
	docker compose run --rm -it persistent-session

persistent-logs:
	docker compose logs -f persistent-session
