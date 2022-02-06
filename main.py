from fastapi import FastAPI

from hotel.db.engine import init_db, DBSession
from hotel.db.models import DBRoom


app = FastAPI()

DB_FILE = "sqlite:///hotel.db"


@app.on_event("startup")
def startup_event():
    init_db(DB_FILE)


@app.get("/")
def read_root():
    return "The server is running."

