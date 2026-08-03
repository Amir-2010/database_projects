
from typing import Union,Optional,Annotated
from pydantic import BaseModel,field_validator,Field
from pydantic import EmailStr,conint,StrictInt,Json
from datetime import datetime
# BaseModel is really important because if there is no BaseModel fastapi can't run

class person(BaseModel):
    name : str
    @field_validator("name")
    def check_name(cls,value): # cls is like self but it is class not obj of class
        if len(value) > 32:
            return "name length is more than 32 character"
        if not value.isalpha():
            return "all the name is not fill with alphabets"
        return value

class person_data(BaseModel):
    id : int
    name : str

# ----------------serialization & deserialization----------------
class users(BaseModel):
    name:str
    password:str

user_num1 = users(name="Amir",password="2010")
# output is like (name="user",password="1234")

user_num1.model_dump() # change to dict type
user_num1.model_dump_json() # change to Json type

# ----------------Filed in pydantic----------------

class Filed_Example_1(BaseModel):
    name:str # ==> this type is str
    data:str # ==> this type is str
    price:float # ==> this type is float
    storage:bool # ==> this type is boolian

class collection_types(BaseModel):
    # when we have more than one data
    users_names:list[str] # now there is a list of str data

class Union_and_Optional(BaseModel):
    user_name: Union[int,str] # Union can't be null and it can have more than one type
    user_age: Optional[int] # Optional can be null

class Specialized_Field(BaseModel):
    # this type of field is unique and just do one special work
    email:EmailStr # EmailStr check the email address

class Data_and_time(BaseModel):
    # these are like specialized Field but for time
    user_time:datetime

class Constrained_Types(BaseModel):
    # these are fot limited the variable
    name:conint(gt=3,lt=50) # this line say name must be lessthan 50 and grater than 3

class Strict_Types(BaseModel):
    # this types is like Basic Types
    age:StrictInt # It can't change

class Custom_Types(BaseModel):
    # you are created these kind of Types
    def create_1 (cls,variable:str|None=[None]):
        if "@" in variable:
            raise Json(content={"detail":"Error"})

class Annotated_Types(BaseModel):
    # this kind of type is for add caption or add limited to variable
    name: Annotated[str,Field(min_length=3,max_length=50)]

class Byte_Data(BaseModel):
    data: bytes