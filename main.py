from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional
from models import Users, Destinations, session
from sqlalchemy.orm import joinedload
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins=[
    'http://localhost:3000'
]

app.add_middleware  (
   CORSMiddleware,
   allow_origins = origins,
   allow_credentials = True,
   allow_methods = ["*"],
   allow_headers = ["*"],
)

class UsersSchema(BaseModel):
    id:int
    name:str
    password:str

    class Config:
        orm_mode = True

class UpdateUsersSchema(BaseModel):
    id:Optional[int]
    name:Optional[str]
    password:Optional[str]

    class Config:
        orm_mode = True

class DestinationsSchema(BaseModel):
    id:int
    name:str
    image:str
    description:str
    location:str
    visit_url:str
    interested:bool
    user_id:int

    class Config:
        orm_mode = True

class UpdateDestinationsSchema(BaseModel):
    id:Optional [int]
    name:Optional [str]
    image:Optional [str]
    description:Optional [str]
    location:Optional [str]
    visit_url:Optional [str]
    interested:Optional [bool]
    user_id:Optional [int]

    class Config:
        orm_mode = True
        
    

@app.get('/')
def root():
    return {'message' : 'Welcome User!'}

@app.get('/users')
def get_all_users() -> List[UsersSchema]:
    users = session.query(Users).all()
    return users

@app.get('/destinations')
def get_all_destinations() -> List[DestinationsSchema]:
    destinations = session.query(Destinations).options(joinedload(Destinations.user)).all()
    destinations_schema = [DestinationsSchema.from_orm(destination) for destination in destinations]
    return destinations_schema

@app.post('/destinations')
def add_destinations(destinations: DestinationsSchema)->DestinationsSchema:
    destin = Destinations(**dict(destinations))
    # session.add(destin)
    session.add(destin)
    session.commit()

    return destin

@app.post('/users')
def add_users(users: UsersSchema)->UsersSchema:
    user0 = Users (**dict(users))
    session.add(user0)
    session.commit()
    
    return user0