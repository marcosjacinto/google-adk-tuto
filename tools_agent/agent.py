from google.adk import Agent
from google.adk.tools.google_search_tool import GoogleSearchTool


def estimate_reading_time(text: str, words_per_minute: int = 200) -> str:
    word_count = len(text.split())
    minutes = max(1, round(word_count / words_per_minute))
    return f"Estimated reading time: {minutes} minute(s) for {word_count} words."


google_search = GoogleSearchTool(bypass_multi_tools_limit=True)

root_agent = Agent(
    name="root_agent",
    instruction=(
        "You are a concise research assistant. "
        "Use the google_search tool to provide information."
        "Then, estimate the reading time of the information you found using the estimate_reading_time tool."
    ),
    description="An assistant that can search the web using Google Search.",
    tools=[google_search, estimate_reading_time],
)
