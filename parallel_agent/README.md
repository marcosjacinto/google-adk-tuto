# Parallel Agent (Well Research)

This example runs multiple research agents in parallel and then synthesizes the results.

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
GOOGLE_API_KEY="your-key" poetry run adk web .
```

Then select `parallel_agent` in the web UI.

## Example queries

- "Research drilling best practices, sandstone formation risks, and HSE controls for a 3500m land well."
- "Provide a drilling brief based on parallel research."

## What this does

- Runs three research agents in parallel (drilling, geology, HSE)
- Stores each summary in session state via `output_key`
- Uses a synthesis agent to produce a structured brief
