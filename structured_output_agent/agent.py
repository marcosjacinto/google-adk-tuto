from pydantic import BaseModel, Field

from google.adk import Agent


class IncidentSummary(BaseModel):
    title: str = Field(..., description="Short incident title")
    summary: str = Field(..., description="Two to three sentence summary")
    severity: str = Field(..., description="low | medium | high | critical")
    suspected_components: list[str] = Field(
        ..., description="Services or components likely involved"
    )
    next_steps: list[str] = Field(
        ..., description="Immediate actions for debugging"
    )


root_agent = Agent(
    name="root_agent",
    instruction=(
        "You are an incident triage assistant. "
        "Return responses that match the IncidentSummary schema."
    ),
    description="Produces structured incident summaries.",
    output_schema=IncidentSummary,
)
