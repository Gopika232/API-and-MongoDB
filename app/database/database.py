from motor.motor_asyncio import AsyncIOMotorClient #type: ignore[import]
from dotenv import load_dotenv #type: ignore[import]
import os

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
DATABASE_NAME = os.getenv("DATABASE_NAME")
client = AsyncIOMotorClient(MONGO_URL)
database = client[DATABASE_NAME]
student_collection = database["student"]