from fastapi import FastAPI
from pydantic import BaseModel
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient
import jwt
client = AsyncIOMotorClient("mongodb://localhost:27017")
db = client['employee_management']
collection = db['employees']



def serialize_mongo_object(obj):
    """
    Convert MongoDB objects to JSON-compatible format.
    """
    if isinstance(obj, ObjectId):
        return str(obj)
    if isinstance(obj, dict):
        return {key: serialize_mongo_object(value) for key, value in obj.items()}
    if isinstance(obj, list):
        return [serialize_mongo_object(item) for item in obj]
    return obj

class Employees(BaseModel):
    employee_id : int
    employee_name : str
    employee_joining_data : str
    employee_salary : float

class Users(BaseModel):
    user_id : int
    username : str
    password : str

# employees = []

app = FastAPI()
# app['secret_key'] = "123"

@app.post("/auth/signup")
async def signup(user : Users):
    user_data = {}
    user_data['user_id'] = user.user_id
    user_data['username'] = user.username
    user_data['password'] = user.password
    db['users'].insert_one(user_data)
    return ({"message" : "user created successfully"})


@app.post("/auth/login")
async def login(user_id: int):
    users = await db['users'].find().to_list(length=100)
    serialized_users = serialize_mongo_object(users)
    for auth_user in serialized_users:
        if auth_user['user_id'] == user_id:
            token = jwt.encode(auth_user,"123", algorithm='HS256')
            return token

@app.get("/employees")
async def employees():
    employees = await db["employees"].find().to_list(length=100)
    serialized_employees = serialize_mongo_object(employees)
    print(serialized_employees)
    return {"employees": serialized_employees}

@app.get("/employee/{employee_id}")
async def get_employee(employee_id : int):
    employees = await collection.find().to_list(length=100)
    serialized = serialize_mongo_object(employees)
    
    for employee in serialized:
        if employee['employee_id'] == employee_id:
            return ({"employee" : employee})


@app.post("/create_employee")
async def create_employee(employee : Employees):
    data = {}
    data['employee_id'] = employee.employee_id
    data['employee_name'] = employee.employee_name
    data['joining_date'] = employee.employee_joining_data
    data['employee_salary'] = employee.employee_salary
    collection.insert_one(data)
    return ({"message" : "employee_added", "employee_details": employee})




