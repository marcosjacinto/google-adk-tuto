from google.adk import Agent


root_agent = Agent(
    name="root_agent",
    instruction=(
        "You are a handoff assistant. "
        "Remember key facts from earlier messages in this session and summarize them when asked."
    ),
    description="Helps track handoff notes across sessions.",
)
