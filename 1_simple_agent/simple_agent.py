import asyncio

from google.adk import Agent
from google.adk.runners import InMemoryRunner


async def main() -> None:
    agent = Agent(
        name="simple_agent",
        instruction=(
            "You are a concise tutorial assistant. "
            "Answer with short, clear explanations and avoid bullet lists unless asked."
        ),
    )
    runner = InMemoryRunner(agent=agent, app_name="simple_agent_tutorial")
    await runner.run_debug("Explain what Google ADK is in one sentence.")


if __name__ == "__main__":
    asyncio.run(main())
