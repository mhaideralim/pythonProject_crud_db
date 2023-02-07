from pydantic import BaseModel

class Person(BaseModel):
    id: int
    name: str
    email: str
    height: float






