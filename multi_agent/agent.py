from google.adk.agents import LlmAgent


geology_agent = LlmAgent(
    name="geology_agent",
    description="Provides formation insights and risk notes.",
    instruction=(
        "You are a geology specialist. Provide concise formation context, "
        "lithology notes, and drilling risk flags."
    ),
)


drilling_agent = LlmAgent(
    name="drilling_agent",
    description="Focuses on drilling plan and operations.",
    instruction=(
        "You are a drilling engineer. Provide a short drilling plan, "
        "key parameters, and operational recommendations."
    ),
)


safety_agent = LlmAgent(
    name="safety_agent",
    description="Focuses on HSE risks and controls.",
    instruction=(
        "You are an HSE specialist. Identify safety risks and recommend controls."
    ),
)


root_agent = LlmAgent(
    name="root_agent",
    description="Coordinates well planning across geology, drilling, and HSE.",
    instruction=(
        "You are the well planning coordinator. Delegate to sub-agents as needed "
        "and produce a consolidated answer."
    ),
    sub_agents=[geology_agent, drilling_agent, safety_agent],
)
