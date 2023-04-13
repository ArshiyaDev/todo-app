from fastapi import FastAPI, Request
from bson.objectid import ObjectId
from model import Todo
from db import collection

app = FastAPI()




@app.post("/todos")
async def create_todo(todo: Todo):
    todo_dict = todo.dict()
    result = await collection.insert_one(todo_dict)
    todo_dict["_id"] = str(result.inserted_id)
    return todo_dict

@app.get("/todos")
async def read_todos():
    todos = []
    async for todo in collection.find():
        todo["_id"] = str(todo["_id"])
        todos.append(todo)
    return todos

@app.put("/todos/{todo_id}")
async def update_todo(todo_id: str, completed: bool):
    result = await collection.update_one({"_id": ObjectId(todo_id)}, {"$set": {"completed": completed}})
    if result.modified_count == 1:
        return {"message": "Todo item updated successfully"}
    else:
        return {"error": "Failed to update todo item"}

@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: str):
    result = await collection.delete_one({"_id": ObjectId(todo_id)})
    if result.deleted_count == 1:
        return {"message": "Todo item deleted successfully"}
    else:
        return {"error": "Failed to delete todo item"}
