# Loop Agent (Iterative Drilling Plan)

This example uses `LoopAgent` to iteratively refine a drilling plan until the critic approves it.

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

Then select `loop_agent` in the web UI.

## Example query

"Create a drilling plan for well W-909 in Gamma Field to 2800 m. Include casing points, mud weight range, and HSE controls."

## What this does

- Drafts an initial drilling plan
- Critiques the plan for gaps and risks
- Refines the plan in a loop until it passes or hits the iteration limit
