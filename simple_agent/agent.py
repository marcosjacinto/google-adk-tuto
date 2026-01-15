from google.adk import Agent


root_agent = Agent(
    name="root_agent",
    instruction=(
        "You are a concise tutorial assistant. "
        "Answer with short, clear explanations and avoid bullet lists unless asked."
    ),
)
