from pymongo.synchronous.database import Database  # for type hints
from dotenv import load_dotenv
from pymongo import MongoClient
import os

load_dotenv()

URI = os.getenv("MONGODB_URI")
assert URI is not None


def print_events():
    """Use example"""
    db = get_db()
    coll_events = db["events"]

    for event in coll_events.find():
        print(event)


def get_db() -> Database:
    client = MongoClient(URI)
    db = client["showup_events"]
    return db


if __name__ == "__main__":
    print_events()  # use example
