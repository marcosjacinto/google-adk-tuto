# Stateful Multi-Agent Well Planning

This example combines stateful session data with a multi-agent setup for well drilling.

## Prerequisites

- Python 3.11
- Poetry
- A Gemini API key exported as `GOOGLE_API_KEY`

## Install dependencies

```bash
poetry install
```

## Run (web)

```bash
GOOGLE_API_KEY="your-key" poetry run adk web .
```

Then select `stateful_multi_agent` in the web UI.

## Run (script)

```bash
GOOGLE_API_KEY="your-key" poetry run python -m stateful_multi_agent.run_stateful
```

## Example prompts

- "Set the well profile to W-777 in Delta Field at 4100 meters."
- "Move to drilling phase and log event: 2026-03-01T08:00Z spud started."
- "Give me a consolidated plan with geology, drilling, and HSE risks."

## What this does

- Stores well details, phase, and events in session state
- Uses a coordinator agent with geology, drilling, and safety sub-agents
- Delegates analysis while keeping shared state across turns
