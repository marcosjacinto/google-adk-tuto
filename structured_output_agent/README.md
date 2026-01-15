# Structured Output Agent

This agent returns structured JSON responses using an output schema.

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

Then select `structured_output_agent` in the web UI.

## Example prompt

"Summarize this incident: payments failed for EU customers between 09:10 and 09:30 UTC with PermissionError: missing scope payments.write.

2026-02-03T14:18:41Z INFO api-gateway request_id=9a1c2f33 method=POST path=/v2/payments status=500 latency_ms=912
2026-02-03T14:18:41Z ERROR payments-service request_id=9a1c2f33 error="PermissionError: missing scope payments.write" region=eu-west-1
2026-02-03T14:18:42Z ERROR payments-service request_id=9a1c2f33 Traceback (most recent call last):
2026-02-03T14:18:42Z ERROR payments-service request_id=9a1c2f33   File "payments.py", line 58, in capture
2026-02-03T14:18:42Z ERROR payments-service request_id=9a1c2f33     authorize_payment(payload)
2026-02-03T14:18:42Z ERROR payments-service request_id=9a1c2f33 PermissionError: missing scope payments.write
2026-02-03T14:18:45Z WARN billing-service request_id=9a1c2f33 msg="payment retries exhausted" attempts=3
2026-02-03T14:18:50Z INFO api-gateway request_id=9a1c2f33 msg="returning error to client" status=502"


## What this does

- Defines an `IncidentSummary` pydantic model
- Uses `output_schema` so the agent responds with structured JSON
- Keeps the agent tool-free for predictable output
