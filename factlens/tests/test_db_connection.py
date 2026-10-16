from sqlalchemy import text

from src.core.database import engine


def test_database_connection():
    try:
        with engine.connect() as connection:
            result = connection.execute(text("SELECT 1"))
            print("Supabase connection successful!")
            print("Query result:", result.scalar_one())

    except Exception as e:
        print("Database connection failed!")
        print(f"Error: {e}")

    finally:
        engine.dispose()


if __name__ == "__main__":
    test_database_connection()