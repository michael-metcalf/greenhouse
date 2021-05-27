from dotenv import load_dotenv
import os
from sqlalchemy import create_engine, text

load_dotenv()

DB_USER = os.environ.get("DB_USER")
DB_PASSWORD = os.environ.get("DB_PASSWORD")

engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@localhost:5432/test", echo=True)

with engine.connect() as conn:
    conn.execute(text("INSERT INTO test_table(x, y) VALUES (:x, :y)"))
    conn.commit()