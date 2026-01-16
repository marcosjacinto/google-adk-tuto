import asyncio

from google.genai import types

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService

from manual_session_agent.agent import root_agent


async def run() -> None:
    session_service = InMemorySessionService()
    runner = Runner(
        app_name="manual_session_agent",
        agent=root_agent,
        session_service=session_service,
    )

    user_id = "demo_user"
    session_id = "demo_session"

    await session_service.create_session(
        app_name="manual_session_agent",
        user_id=user_id,
        session_id=session_id,
        state={"well_id": "W-201", "operator": "PetroCo"},
    )

    message = types.Content(
        role="user",
        parts=[types.Part(text="Summarize the well context and operator.")],
    )

    async for event in runner.run_async(
        user_id=user_id,
        session_id=session_id,
        new_message=message,
        state_delta={"status": "monitoring"},
    ):
        if event.is_final_response():
            parts = event.content.parts if event.content else []
            text = "\n".join(part.text for part in parts if part.text)
            print(text)


if __name__ == "__main__":
    asyncio.run(run())
