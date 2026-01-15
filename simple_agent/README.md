# Simple Agent (No Tools)

This example shows the smallest ADK agent: a single LLM agent with an instruction and no tools.

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
GOOGLE_API_KEY="your-key" poetry run adk web simple_agent
```

## What this does

- Creates a single `root_agent` with a short instruction
- Exposes `agent.py` so `adk web` can load the agent module
- Lets you chat with the agent in the web UI
