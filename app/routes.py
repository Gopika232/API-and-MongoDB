from fastapi import APIRouter,HTTPException,status #type: ignore[import]
from app.models import Student,UpdateFull,PartialUpdate
from app.services import *

router = APIRouter(prefix = "/students", tags = ["Students"])

@router.get("/")

async def get_students():
    students = await get_all_students()
    return {
        "success":True,
        "data" : students
    }

@router.post("/",status_code=status.HTTP_201_CREATED)
async def add_student(student:Student):
    existing_student = await get_student_by_id(student.id)
    if existing_student:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Student with this ID already exists.")
    
    await create_student(student.dict())
    return {
        "success":True,
        "message" :"Student Added Successfully"
    }

@router.get("/{student_id}")
async def get_specific_student(student_id : int):

    student = await get_student_by_id(student_id)

    if not student:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found.")
    
    student["_id"] = str(student["_id"])

    return {
        "success":True,
        "data" : student
    }

@router.put("/{student_id}")

async def update_entire_student(student_id:int ,student : UpdateFull):

    result = await update_student(student_id,student.dict())

    if result.matched_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found.")

    return {
        "success":True,
        "message" :"Student Updated Successfully"
    }

@router.patch("/{student_id}")

async def update_partial_student(student_id : int , student : PartialUpdate):

    update_data = student.dict(exclude_unset = True)

    result = await update_student(student_id,update_data)

    if result.matched_count == 0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found.")
    
    return {
        "success":True,
        "message" :"Student Updated Successfully"
    }

@router.delete("/{student_id}")

async def delete_specific_student(student_id : int):

    result = await delete_student(student_id)

    if result.deleted_count ==0:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Student not found.")
    
    return {
        "success":True,
        "message" :"Student Deleted Successfully"
    }

@router.get("/search/") 

async def search(name: str = None, course: str = None):
    students = await search_students(name, course)

    return {
        "success":True,
        "data" : students
    }