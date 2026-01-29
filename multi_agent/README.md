# Multi-Agent Well Planning

This example coordinates multiple agents to produce a consolidated well drilling plan.

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

Then select `multi_agent` in the web UI.

## Example prompt

"We plan to drill Well W-402 in Alpha Field to 3,200 m. Provide a concise drilling plan, geology risks, and HSE controls."

## What this does

- Uses a coordinator agent with three sub-agents
- Delegates geology, drilling, and safety inputs
- Returns a single consolidated response
