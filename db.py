from motor.motor_asyncio import AsyncIOMotorClient



client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client["todo_db"]
collection = db["todos"]

