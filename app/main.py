from fastapi import FastAPI
from app.routers import books
from app.database.db import engine
from app.database.base import Base
import app.models.book
import time

app = FastAPI()

# DB接続リトライ
for i in range(10):
    try:
        Base.metadata.create_all(bind=engine)
        print("DB connected")
        break
    except Exception as e:
        print("DB not ready, retrying...")
        time.sleep(3)

app.include_router(books.router)

@app.get("/")
def root():
    return {"message": "Reading Tracker API"}