
import os
from pathlib import Path

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL

# Locate the outer FactLens project directory
PROJECT_ROOT = Path(__file__).resolve().parents[3]

# Load the .env file from the project root
load_dotenv(PROJECT_ROOT / ".env", override=True)

# Read database configuration
USER = os.getenv("user")
PASSWORD = os.getenv("password")
HOST = os.getenv("host")
PORT = os.getenv("port", "5432")
DBNAME = os.getenv("dbname", "postgres")

if not all([USER, PASSWORD, HOST, PORT, DBNAME]):
    raise ValueError(
        "Database configuration is incomplete. "
        "Check user, password, host, port, and dbname in .env."
    )

# Build a safely escaped PostgreSQL connection URL
DATABASE_URL = URL.create(
    drivername="postgresql+psycopg2",
    username=USER,
    password=PASSWORD,
    host=HOST,
    port=int(PORT),
    database=DBNAME,
    query={"sslmode": "require"},
)

engine = create_engine(DATABASE_URL)

def test_connection():
    try:
        with engine.connect() as connection:
            connection.exec_driver_sql("SELECT 1")
            print("Database connection successful!")
    except Exception as e:
        print(f"Database connection failed: {e}")
        raise
