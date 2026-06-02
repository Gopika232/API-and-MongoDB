from pydantic import BaseModel,EmailStr  # type: ignore[import]
from typing import Optional

class Student(BaseModel):
    id : int
    name : str
    email :  EmailStr
    course : str

class UpdateFull(BaseModel):
    name: str
    email: EmailStr
    course: str

class PartialUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[EmailStr] = None
    course: Optional[str] = None