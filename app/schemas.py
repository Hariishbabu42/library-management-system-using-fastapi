from pydantic import BaseModel

class RegisterBooks(BaseModel):
    book_id : int
    book_title : str
    book_description : str
    category : str

class BooksResponse(BaseModel):
    book_id : int
    book_title : str
    availability : str

class CreateUser(BaseModel):
    user_id : int
    username : str
    department : str

class GetUser(BaseModel):
    user_id : int
    username : str
    department : str
    pending_dues : float