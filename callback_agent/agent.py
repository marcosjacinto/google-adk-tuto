from __future__ import annotations

from datetime import datetime, timezone

from google.adk.agents.callback_context import CallbackContext
from google.adk.agents.llm_agent import LlmAgent
from google.adk.models.llm_request import LlmRequest
from google.adk.models.llm_response import LlmResponse
from google.adk.tools.base_tool import BaseTool
from google.adk.tools.tool_context import ToolContext


def before_model(callback_context: CallbackContext, llm_request: LlmRequest) -> None:
    callback_context.state["last_request_at"] = datetime.now(timezone.utc).isoformat()
    callback_context.state["last_request_model"] = llm_request.model


def after_model(callback_context: CallbackContext, llm_response: LlmResponse) -> None:
    callback_context.state["last_response_at"] = datetime.now(timezone.utc).isoformat()
    if llm_response.content and llm_response.content.parts:
        first_text = next(
            (part.text for part in llm_response.content.parts if part.text), ""
        )
        callback_context.state["last_response_preview"] = first_text[:120]


def record_pressure(well_id: str, timestamp: str, psi: float) -> dict:
    return {"well_id": well_id, "timestamp": timestamp, "psi": psi}


def compute_pressure_drop(start_psi: float, end_psi: float) -> dict:
    drop = start_psi - end_psi
    percent = (drop / start_psi) * 100 if start_psi else 0.0
    return {"drop_psi": drop, "drop_percent": round(percent, 2)}


def format_well_alert(well_id: str, message: str, severity: str = "medium") -> dict:
    return {"well_id": well_id, "severity": severity, "message": message}


def before_tool(
    tool: BaseTool, args: dict, tool_context: ToolContext
) -> dict:
    tool_context.state["last_tool_name"] = tool.name
    tool_context.state["last_tool_args"] = args
    tool_context.state["last_tool_started_at"] = datetime.now(timezone.utc).isoformat()
    return args


def after_tool(
    tool: BaseTool,
    args: dict,
    tool_context: ToolContext,
    tool_response: dict,
) -> dict:
    tool_context.state["last_tool_finished_at"] = datetime.now(timezone.utc).isoformat()
    tool_context.state["last_tool_output_preview"] = str(tool_response)[:120]
    return tool_response


root_agent = LlmAgent(
    name="root_agent",
    description="Well monitoring assistant with callback auditing.",
    instruction=(
        "You are a well monitoring assistant. Use tools to record readings, "
        "calculate pressure drops, and format alerts."
    ),
    tools=[record_pressure, compute_pressure_drop, format_well_alert],
    before_model_callback=before_model,
    after_model_callback=after_model,
    before_tool_callback=before_tool,
    after_tool_callback=after_tool,
)
