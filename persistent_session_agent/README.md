# Persistent Session Agent (SQLite)

This agent captures handoff notes and recalls them across sessions.

## Prerequisites

- Python 3.11
- Poetry
- A Gemini API key exported as `GOOGLE_API_KEY`

## Install dependencies

```bash
poetry install
```

## Run

```bash
GOOGLE_API_KEY="your-key" ADK_SQLITE_PATH="/app/data/sessions.db" \
  poetry run python -m persistent_session_agent.run_persistent
```

To recall the stored handoff, run again with:

```bash
ADK_RUN_MODE=recall GOOGLE_API_KEY="your-key" ADK_SQLITE_PATH="/app/data/sessions.db" \
  poetry run python -m persistent_session_agent.run_persistent
```

## Docker

This repo mounts a volume at `/app/data` for the SQLite file. Use the `persistent-session` service in `docker-compose.yml`.

```bash
docker compose up persistent-session
```

## What this does

- Stores handoff notes in the same session ID across runs
- Recalls notes on demand using session history
- Uses a SQLite-backed session service under the hood
