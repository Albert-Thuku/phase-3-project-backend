from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from models import Users, Destinations, session
from sqlalchemy.orm import joinedload
from sqlalchemy import distinct

app = FastAPI()

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
    category:str
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
    category:Optional [str]
    location:Optional [str]
    visit_url:Optional [str]
    interested:Optional [bool]
    user_id:Optional [int]

    class Config:
        orm_mode = True

@app.get('/')
def root():
    return {'message' : 'Welcome User!'}

#Returns all users 
@app.get('/users')
def get_all_users() -> List[UsersSchema]:
    users = session.query(Users).all()
    return users

#returns all destinations
@app.get('/destinations')
def get_all_destinations() -> List[DestinationsSchema]:
    destinations = session.query(Destinations).options(joinedload(Destinations.user)).all()
    destinations_schema = [DestinationsSchema.from_orm(destination) for destination in destinations]
    return destinations_schema

#updates user information
@app.patch('/update/user/{id}')
def update_user(id:int, payload: UpdateUsersSchema) -> UsersSchema:
    updated_user = session.query(Users).filter_by(id = id).first()
    if not updated_user:
        raise HTTPException(status_code=404, detail=f'The user with id {id} does not exist')
    for key, value in payload.dict(exclude_unset=True).items():
        setattr(updated_user, key, value)
    session.commit()
    return updated_user

#updates destination information
@app.patch('update/destination/{id}')
def update_destination(id:int, payload: UpdateDestinationsSchema) -> DestinationsSchema:
    updated_destination = session.query(Destinations).filter_by(id=id).first()
    if not updated_destination:
        raise HTTPException(status_code=404, detail=f'The destination with id {id} does not exist')
    for key, value in payload.dict(exclude_unset=True).items():
        setattr(updated_destination, key, value)
    session.commit()
    return updated_destination