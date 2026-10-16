from sqlalchemy import inspect, select

from src.core.database import engine, SessionLocal
from src.models.Conversation import Conversation


def test_conversation_table():
    inspector = inspect(engine)

    assert inspector.has_table(
        "conversations",
        schema="public",
    ), "The conversations table does not exist."

    with SessionLocal() as db:
        result = db.execute(
            select(Conversation).limit(5)
        )
        conversations = result.scalars().all()

        print("Conversation table exists.")
        print(f"Records found: {len(conversations)}")


if __name__ == "__main__":
    try:
        test_conversation_table()
    except Exception as exc:
        print(f"Test failed: {exc}")
        raise
    finally:
        engine.dispose()