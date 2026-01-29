# Stateful Tools Agent

This agent tracks well data in session state for analysis.

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

Then select `stateful_tools_agent` in the web UI.

## Example prompts

- "Set well metadata for W-101 in Alpha Field, offshore ES, operator PetroCo."
- "Add pressure reading 3250 psi at 2026-02-10T09:15:00Z."
- "Add flow rate 1850 bpd at 2026-02-10T09:15:00Z."
- "Log maintenance event: replaced choke valve at 2026-02-10T12:30:00Z."
- "Show me the well snapshot."
- "Reset the well state."

## What this does

- Uses tool functions that mutate `tool_context.state`
- Persists well metadata, readings, and events across turns
- Produces a snapshot with averages for quick analysis
