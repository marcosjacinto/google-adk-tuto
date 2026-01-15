from google.adk import Agent
from google.adk.tools.tool_context import ToolContext


def set_well_metadata(
    well_id: str,
    field: str,
    location: str,
    operator: str,
    tool_context: ToolContext,
) -> str:
    tool_context.state["well_metadata"] = {
        "well_id": well_id,
        "field": field,
        "location": location,
        "operator": operator,
    }
    return f"Stored metadata for well {well_id}."


def add_pressure_reading(
    timestamp: str,
    psi: float,
    tool_context: ToolContext,
) -> str:
    readings = tool_context.state.get("pressure_readings", [])
    readings.append({"timestamp": timestamp, "psi": psi})
    tool_context.state["pressure_readings"] = readings
    return f"Added pressure reading: {psi} psi at {timestamp}."


def add_flow_rate(
    timestamp: str,
    barrels_per_day: float,
    tool_context: ToolContext,
) -> str:
    rates = tool_context.state.get("flow_rates", [])
    rates.append({"timestamp": timestamp, "barrels_per_day": barrels_per_day})
    tool_context.state["flow_rates"] = rates
    return f"Added flow rate: {barrels_per_day} bpd at {timestamp}."


def add_maintenance_event(
    timestamp: str,
    description: str,
    tool_context: ToolContext,
) -> str:
    events = tool_context.state.get("maintenance_events", [])
    events.append({"timestamp": timestamp, "description": description})
    tool_context.state["maintenance_events"] = events
    return "Logged maintenance event."


def get_well_snapshot(tool_context: ToolContext) -> dict:
    metadata = tool_context.state.get("well_metadata", {})
    pressure = tool_context.state.get("pressure_readings", [])
    flow_rates = tool_context.state.get("flow_rates", [])
    maintenance = tool_context.state.get("maintenance_events", [])
    avg_pressure = (
        sum(p["psi"] for p in pressure) / len(pressure) if pressure else None
    )
    avg_flow = (
        sum(r["barrels_per_day"] for r in flow_rates) / len(flow_rates)
        if flow_rates
        else None
    )
    return {
        "metadata": metadata,
        "pressure_readings": pressure,
        "flow_rates": flow_rates,
        "maintenance_events": maintenance,
        "avg_pressure_psi": avg_pressure,
        "avg_flow_bpd": avg_flow,
    }


def reset_well_state(tool_context: ToolContext) -> str:
    tool_context.state.clear()
    return "Well session state cleared."


root_agent = Agent(
    name="root_agent",
    instruction=(
        "You are a well analysis assistant. "
        "Use tools to record well metadata, readings, and events, "
        "then summarize the current well state when asked."
    ),
    description="Tracks well details in session state for analysis.",
    tools=[
        set_well_metadata,
        add_pressure_reading,
        add_flow_rate,
        add_maintenance_event,
        get_well_snapshot,
        reset_well_state,
    ],
)
