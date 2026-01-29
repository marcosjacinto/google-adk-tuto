# Agent With Tools

This example adds a built-in tool so the agent can fetch fresh information.

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

Then select `tools_agent` in the web UI.

## What this does

- Defines a `root_agent` that can call the `google_search` tool
- Lets the model decide when to search for up-to-date info
- Uses `adk web` to run the agent alongside the others in this repo
