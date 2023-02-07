from pydantic import BaseModel
import asyncio

class Person(BaseModel):
    id: int
    name: str
    email: str
    height: float






