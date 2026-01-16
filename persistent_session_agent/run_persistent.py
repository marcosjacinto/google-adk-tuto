import asyncio
import os
import sys

from google.genai import types

from google.adk.runners import Runner
from google.adk.sessions import DatabaseSessionService

from persistent_session_agent.agent import root_agent


async def run() -> None:
    db_path = os.getenv("ADK_SQLITE_PATH", "/app/data/sessions.db")
    db_url = f"sqlite+aiosqlite:///{db_path}"
    session_service = DatabaseSessionService(db_url)
    runner = Runner(
        app_name="persistent_session_agent",
        agent=root_agent,
        session_service=session_service,
    )

    user_id = "demo_user"
    session_id = "persistent_session"

    session = await session_service.get_session(
        app_name="persistent_session_agent",
        user_id=user_id,
        session_id=session_id,
    )
    if not session:
        await session_service.create_session(
            app_name="persistent_session_agent",
            user_id=user_id,
            session_id=session_id,
            state={"started": True},
        )

    if not sys.stdin.isatty():
        user_text = os.getenv("ADK_MESSAGE", "").strip()
        if not user_text:
            print("No TTY available. Set ADK_MESSAGE to send a single prompt.")
            return
        messages = [user_text]
    else:
        print("Persistent session chat. Type 'exit' to quit.")
        messages = None

    while True:
        if messages is not None:
            if not messages:
                break
            user_text = messages.pop(0)
        else:
            user_text = input("> ").strip()
            if not user_text or user_text.lower() in {"exit", "quit"}:
                break

        message = types.Content(
            role="user",
            parts=[types.Part(text=user_text)],
        )

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
