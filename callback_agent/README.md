# Callback Agent

This agent uses model callbacks to capture request/response metadata in session state.

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

Then select `callback_agent` in the web UI.

## Example prompts

- "Record pressure 3120 psi for well W-901 at 2026-04-03T09:20:00Z."
- "Compute pressure drop from 3250 to 3010 psi."
- "Create a high severity alert for well W-901: sudden pressure drop detected."

## What this does

- Provides well monitoring tools for pressure readings and alerts
- Writes `last_request_at` and `last_request_model` in `before_model`
- Writes `last_response_at` and a short `last_response_preview` in `after_model`
- Writes `last_tool_*` fields in `before_tool` and `after_tool`
