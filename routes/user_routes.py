from fastapi import APIRouter
from models.user_model import User
from schemas.user_schema import users_serializer
from bson.objectid import ObjectId
from config.db import collection

user = APIRouter()

@user.post("/")
async def create_user(user: User):
    _id = collection.insert_one(dict(user))
    user = users_serializer(collection.find({"_id": _id.inserted_id}))
    return {"status": "Ok","data": user}

@user.get("/")
async def find_all_users():
    users = users_serializer(collection.find())
    return {"status": "Ok","data": users}

@user.get("/{id}")
async def get_one_user(id: str):
    user = users_serializer(collection.find({"_id": ObjectId(id)}))
    return {"status": "Ok","data": user}

@user.put("/{id}")
async def update_user(id: str, user: User):
    collection.find_one_and_update(
        {
            "_id": ObjectId(id)
        }, 
        {
            "$set": dict(user)
        })
    user = users_serializer(collection.find({"_id": ObjectId(id)}))
    return {"status": "Ok","data": user}

@user.delete("/{id}")
async def delete_user(id: str):
    collection.find_one_and_delete({"_id": ObjectId(id)})
    users = users_serializer(collection.find())
    return {"status": "Ok","data": []} 