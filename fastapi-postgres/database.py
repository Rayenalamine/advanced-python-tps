from sqlalchemy import create_engine

DATABASE_URL = "postgresql://postgres:admin@localhost/fastapi_db"

engine = create_engine(DATABASE_URL)