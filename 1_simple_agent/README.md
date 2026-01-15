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
GOOGLE_API_KEY="your-key" poetry run python 1_simple_agent/simple_agent.py
```

## What this does

- Creates a single `Agent` with a short instruction
- Uses `InMemoryRunner` for a quick debug run
- Sends one user prompt and prints the response to the console
