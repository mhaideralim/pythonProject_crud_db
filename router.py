from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from db_connection import person_data
from model import Person

app = FastAPI()


@app.get("/get-data/{name}")
async def get_data(name: str):
    data = person_data.find_one({"name":name})
    if data:
        return data
    else:
        raise HTTPException(status_code=404, detail="Dictionary not found")


@app.post("/set-data/{id}")
async def set_data(id: int, persons: Person):
    if  person_data.find_one({"id": id}):
            return {"message": "ID already exists"}
    else:
        person_data.insert_one(persons.dict())
        return {"message": "Data inserted successfully"}


@app.put("/update_data/{id}")
async def update_data(id: int, new_data: Person):
    if person_data.find_one({"id": id}):
        return person_data.update_one({"id": id}, {"$set": new_data.dict()}),{"data updated successfully"}
    else:
        raise HTTPException(status_code=404, detail="Data not found")



@app.delete("/delete-data/{id}")
async def delete_data(id: int):
    if person_data.find_one({"id": id}):
        result = person_data.delete_one({"id": id})

    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="Data not found")

    return {"message": "Data deleted successfully"}
