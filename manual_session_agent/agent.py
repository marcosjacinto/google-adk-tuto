from google.adk import Agent


root_agent = Agent(
    name="root_agent",
    instruction=(
        "You are a well analysis assistant for well {well_id}. "
        "Use the latest session state values when answering questions."
    ),
    description="Demonstrates session state placeholders in instructions.",
)
