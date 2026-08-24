from motor.motor_asyncio import AsyncIOMotorClient

from config import *

client = AsyncIOMotorClient(MONGODB_URL)

db = client[DATABASE_NAME]

users = db.users

messages = db.messages

sessions = db.sessions

feedback = db.feedback