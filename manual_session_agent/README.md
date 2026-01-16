# Manual Session + Runner Agent

This example manually wires a `Runner` and `SessionService` to show state handling.

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
GOOGLE_API_KEY="your-key" poetry run python -m manual_session_agent.run_manual
```

## What this does

- Creates an `InMemorySessionService` and `Runner` explicitly
- Seeds session state (`well_id`, `operator`) before the run
- Uses a `{well_id}` placeholder in the agent instruction
- Applies a `state_delta` during the invocation
