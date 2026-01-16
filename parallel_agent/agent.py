from google.adk.agents import LlmAgent, ParallelAgent, SequentialAgent
from google.adk.tools.google_search_tool import GoogleSearchTool


google_search = GoogleSearchTool()


drilling_research_agent = LlmAgent(
    name="DrillingResearchAgent",
    description="Researches drilling best practices.",
    instruction=(
        "You are a drilling research assistant. "
        "Research best practices for drilling a land well to 3500m. "
        "Use Google Search and summarize in 1-2 sentences. Output only the summary."
    ),
    tools=[google_search],
    output_key="drilling_research",
)


geology_research_agent = LlmAgent(
    name="GeologyResearchAgent",
    description="Researches common formation risks.",
    instruction=(
        "You are a geology research assistant. "
        "Research common formation risks for sandstone reservoirs. "
        "Use Google Search and summarize in 1-2 sentences. Output only the summary."
    ),
    tools=[google_search],
    output_key="geology_research",
)


hse_research_agent = LlmAgent(
    name="HseResearchAgent",
    description="Researches HSE controls for drilling operations.",
    instruction=(
        "You are an HSE research assistant. "
        "Research key HSE controls for drilling operations. "
        "Use Google Search and summarize in 1-2 sentences. Output only the summary."
    ),
    tools=[google_search],
    output_key="hse_research",
)


parallel_research_agent = ParallelAgent(
    name="ParallelWellResearchAgent",
    description="Runs drilling, geology, and HSE research in parallel.",
    sub_agents=[
        drilling_research_agent,
        geology_research_agent,
        hse_research_agent,
    ],
)


synthesis_agent = LlmAgent(
    name="SynthesisAgent",
    description="Synthesizes research findings into a drilling brief.",
    instruction=(
        "You are a drilling coordinator. Synthesize the following summaries into a "
        "structured brief with headings. Only use the provided inputs.\n\n"
        "Drilling Research:\n{drilling_research}\n\n"
        "Geology Research:\n{geology_research}\n\n"
        "HSE Research:\n{hse_research}\n\n"
        "Output format:\n"
        "## Drilling Brief\n"
        "### Drilling Practices\n"
        "### Formation Risks\n"
        "### HSE Controls\n"
        "### Conclusion\n"
    ),
)


root_agent = SequentialAgent(
    name="root_agent",
    description="Coordinates parallel research and synthesis.",
    sub_agents=[parallel_research_agent, synthesis_agent],
)
