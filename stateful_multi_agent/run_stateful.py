import asyncio

from google.genai import types

from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService

from stateful_multi_agent.agent import root_agent


async def run() -> None:
    session_service = InMemorySessionService()
    runner = Runner(
        app_name="stateful_multi_agent",
        agent=root_agent,
        session_service=session_service,
    )

    user_id = "demo_user"
    session_id = "stateful_session"

    session = await session_service.get_session(
        app_name="stateful_multi_agent",
        user_id=user_id,
        session_id=session_id,
    )
    if not session:
        await session_service.create_session(
            app_name="stateful_multi_agent",
            user_id=user_id,
            session_id=session_id,
            state={
                "well_profile": {
                    "well_id": "W-501",
                    "field": "Bravo Field",
                    "target_depth_m": 3200,
                },
                "current_phase": "planning",
                "events": [],
            },
        )

    print("Stateful multi-agent chat. Type 'exit' to quit.")
    while True:
        user_text = input("> ").strip()
        if not user_text or user_text.lower() in {"exit", "quit"}:
            break

        message = types.Content(role="user", parts=[types.Part(text=user_text)])
        async for event in runner.run_async(
            user_id=user_id,
            session_id=session_id,
            new_message=message,
        ):
            if event.is_final_response():
                parts = event.content.parts if event.content else []
                text = "\n".join(part.text for part in parts if part.text)
                if text:
                    print(text)


if __name__ == "__main__":
    asyncio.run(run())
