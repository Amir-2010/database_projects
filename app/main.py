
from fastapi import FastAPI,status
from fastapi.responses import JSONResponse as J
from schemas import person,person_data
# from typing import List

users = [{"id": 1,"name": "John"},
         {"id": 2,"name": "Emma"},
         {"id": 3,"name": "Michael"},
         {"id": 4,"name": "Sophia"},
         {"id": 5,"name": "Daniel"},
         {"id": 6,"name": "Olivia"},
         {"id": 7,"name": "James"},
         {"id": 8,"name": "Isabella"},
         {"id": 9,"name": "William"},
         {"id": 10,"name": "Charlotte"}]

app = FastAPI()

@app.get("/")
def show_users():
    return users

@app.post("/")
def create_name(user_name:person):
    if user_name.name:
        if user_name.name == "name length is more than 32 character":
            return J(content="name length is more than 32 character",status_code=status.HTTP_201_CREATED)
        elif user_name.name == "all the name is not fill with alphabets":
            return J(content="all the name is not fill with alphabets",status_code=status.HTTP_201_CREATED)
        else:
            users.append({"id": len(users)+1,"name": user_name.name})
            return J(content=users[-1],status_code=status.HTTP_201_CREATED)
    
    else:
        return J(content={"detail":user_name},status_code=status.HTTP_422_UNPROCESSABLE_CONTENT)

# if we don't use List from typing the program think there is just one data not a list
# then we have error
@app.get("/with_response_model",response_model=list[person_data])
def show_users():
    return users