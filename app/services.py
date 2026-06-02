from app.database import student_collection
async def get_all_students():
    students=[]
    async for student in student_collection.find():
        student["_id"] = str(student["_id"])
        students.append(student)
    return students

async def create_student(student):
    await student_collection.insert_one(student)
    return student

async def get_student_by_id(student_id : int):
    return await student_collection.find_one({"id":student_id})

async def delete_student(student_id : int):
    return await student_collection.delete_one({"id":student_id})

async def update_student(student_id : int , data:dict):
    return await student_collection.update_one({"id":student_id},{"$set":data})

async def search_students(name: str = None, course: str = None):
    query = {}
    if name:
        query["name"] = {"$regex": name, "$options": "i"}
    if course:
        query["course"] = {"$regex": course, "$options": "i"}

    students = []
    async for student in student_collection.find(query):
        student["_id"] = str(student["_id"])
        students.append(student)
    return students