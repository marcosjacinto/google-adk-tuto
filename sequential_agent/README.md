# Sequential Agent

This example uses `SequentialAgent` to run three agents in a fixed sequence: design → review → refactor.

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

Then select `sequential_agent` in the web UI.

## Example queries

- "Plan a drilling program for well W-888 in Delta Field to 3600 meters."
- "Include key drilling parameters and a short checklist."
- "Design a drilling program for well W-888 in Delta Field to 3600 m. Include casing points, mud weight range, BOP tests, and a short contingency plan for lost circulation. Then review for risks and refactor into a final program."

## What this does

- Uses `SequentialAgent` to orchestrate sub-agents
- Runs `DesignAgent` to write the draft program (`draft_program`)
- Runs `ReviewAgent` to generate review notes (`review_notes`)
- Runs `RefactorAgent` to produce the final program (`final_program`)
