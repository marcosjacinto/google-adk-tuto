from google.adk.agents import LlmAgent
from google.adk.tools.tool_context import ToolContext


def set_well_profile(
    well_id: str,
    field: str,
    target_depth_m: int,
    tool_context: ToolContext,
) -> str:
    tool_context.state["well_profile"] = {
        "well_id": well_id,
        "field": field,
        "target_depth_m": target_depth_m,
    }
    return f"Stored well profile for {well_id}."


def update_phase(phase: str, tool_context: ToolContext) -> str:
    tool_context.state["current_phase"] = phase
    return f"Updated phase to {phase}."


def log_event(timestamp: str, note: str, tool_context: ToolContext) -> str:
    events = tool_context.state.get("events", [])
    events.append({"timestamp": timestamp, "note": note})
    tool_context.state["events"] = events
    return "Logged event."


def get_state_snapshot(tool_context: ToolContext) -> dict:
    return tool_context.state.to_dict()


geology_agent = LlmAgent(
    name="geology_agent",
    description="Provides formation context and geology risks.",
    instruction=(
        "You are a geology specialist for well {well_profile.well_id}. "
        "Use the current phase {current_phase} and identify geology risks."
    ),
)


drilling_agent = LlmAgent(
    name="drilling_agent",
    description="Focuses on drilling operations and parameters.",
    instruction=(
        "You are a drilling engineer for well {well_profile.well_id}. "
        "Use the target depth {well_profile.target_depth_m}m and phase {current_phase}."
    ),
)


safety_agent = LlmAgent(
    name="safety_agent",
    description="Highlights HSE risks and mitigations.",
    instruction=(
        "You are an HSE specialist for well {well_profile.well_id}. "
        "Review recent events and call out safety controls."
    ),
)


root_agent = LlmAgent(
    name="root_agent",
    description="Coordinates stateful well planning across sub-agents.",
    instruction=(
        "You are the well planning coordinator. Keep the session state updated. "
        "Always delegate to geology_agent, drilling_agent, and safety_agent for analysis "
        "before producing the final response. "
        "When the user provides new well details, call the appropriate tools. "
        "Synthesize sub-agent inputs into a single response."
    ),
    tools=[set_well_profile, update_phase, log_event, get_state_snapshot],
    sub_agents=[geology_agent, drilling_agent, safety_agent],
)
