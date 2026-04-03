from fastapi import FastAPI


app = FastAPI()

# 路径参数和查询参数

# http://localhost:8000/
# {"message": "Hello World!"}
@app.get("/")
async def read_root():
    return {"message": "Hello World!"}

# http://localhost:8000/greet/luv
# {"message": "Hello, luv!"}
@app.get('/greet/{name}')
async def greet_name(name: str) -> dict:
    return {"message": f"Hello, {name}!"}

# http://localhost:8000/greetname?name=luv
# {"message": "Hello, your name is luv!"}
@app.get('/greet_name')
async def greet_name(name: str) -> dict:
    return {"message": f"Hello, your name is {name}!"}

# http://localhost:8000/greet_mix/luv?age=20
# {"message": "Hello, luv! You are 20 years old."}
@app.get('/greet_mix/{name}')
async def greet_name_mix(name: str, age: int) -> dict:
    return {"message": f"Hello, {name}! You are {age} years old."}



from typing import Optional
# http://localhost:8000/greet_optional/luv?age=20  
# {"message": "Hello, luv! You are 20 years old."}
# http://localhost:8000/greet_optional/luv
# {"message": "Hello, luv! You are 0 years old."}
# http://localhost:8000/greet_optional/
# {"message": "Hello, User! You are 0 years old."}
@app.get('/greet_optional')
async def greet_name_optional(name:Optional[str] = "User",age:int = 0) -> dict:
    return {"message": f"Hello, {name}! You are {age} years old."}
        
        
# 简单的请求体模型，创建一本书，并返回创建成功的信息
from pydantic import BaseModel

class BookCreateModel(BaseModel):
    title: str
    author: str

@app.post('/create_book')
async def create_book(book_data: BookCreateModel) -> dict:
    return {
        "message": "Book created",
        "title": book_data.title,
        "author": book_data.author,
        
    }
   
# 获得请求头信息
from fastapi import Request, Header
@app.get('/get_headers')
async def get_headers(
    accept: str = Header(None),
    content_type: str = Header(None),
    user_agent: str = Header(None),
    host: str = Header(None),
):
    request_headers = {}
    request_headers["Accept"] = accept
    request_headers["Content-Type"] = content_type
    request_headers["User-Agent"] = user_agent
    request_headers["Host"] = host

    return request_headers
        