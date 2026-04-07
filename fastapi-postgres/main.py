from fastapi import FastAPI
from sqlalchemy import text
from database import engine

app = FastAPI()

# Home
@app.get("/")
def home():
    return {"message": "API is working!"}

# Get all users
@app.get("/users")
def get_users():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM users"))
        users = []
        for row in result:
            users.append({
                "id": row[0],
                "name": row[1],
                "email": row[2]
            })
        return users

# Add user
@app.post("/users")
def add_user(user: dict):
    with engine.begin() as conn:
        conn.execute(
            text("INSERT INTO users (name, email) VALUES (:name, :email)"),
            {"name": user["name"], "email": user["email"]}
        )
    return {"message": "User added"}

# Delete user
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    with engine.begin() as conn:
        conn.execute(
            text("DELETE FROM users WHERE id = :id"),
            {"id": user_id}
        )
    return {"message": "User deleted"}