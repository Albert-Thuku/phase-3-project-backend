from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, validate_arguments
from typing import List, Optional
from models import Users, Destinations, session, Users_Destinations
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins=[
    'http://localhost:3001'
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

    class Config:
        orm_mode = True

class UpdateDestinationsSchema(BaseModel):
    name:Optional [str]
    image:Optional [str]
    description:Optional [str]
    category:Optional [str]
    location:Optional [str]
    visit_url:Optional [str]
    
    class Config:
        orm_mode = True

class InterestSchema(BaseModel):
    id:int
    user_id:int
    destination_id:int

    class Config:
        orm_mode = True

class UpdateInterestSchema(BaseModel):
    user_id:Optional [int]
    destination_id:Optional [int]

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

@app.get('/destinations')
def get_all_destinations() -> List[DestinationsSchema]:
    destinations = session.query(Destinations).all()
    return destinations

#returns all interests
@app.get('/interests')
def get_all_interests():
    interests = session.query(Users_Destinations).all()
    return interests

#create new destination data
@app.post('/update/destinations')
def add_destinations(destinations: UpdateDestinationsSchema)->DestinationsSchema:
    destin = Destinations(**dict(destinations))
    # session.add(destin)
    session.add(destin)
    session.commit()

    return destin 

#create new user data
@app.post('/signup')
@validate_arguments
def add_users(users: UpdateUsersSchema)->UpdateUsersSchema:
    user0 = Users (**dict(users))
    session.add(user0)
    session.commit()
    
    return user0 

#create new interest
@app.post('/update/interests')
def add_interest(interests: UpdateInterestSchema)->InterestSchema:
    interest = Users_Destinations(**dict(interests))
    session.add(interest)
    session.commit()
    return interest

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
@app.patch('/update/destination/{id}')
def update_destination(id:int, payload: UpdateDestinationsSchema) -> DestinationsSchema:
    updated_destination = session.query(Destinations).filter_by(id=id).first()
    if not updated_destination:
        raise HTTPException(status_code=404, detail=f'The destination with id {id} does not exist')
    for key, value in payload.dict(exclude_unset=True).items():
        setattr(updated_destination, key, value)
    session.commit()
    return updated_destination

#updates interest information
@app.patch('/update/interest/{id}')
def update_interest(id:int, payload: UpdateInterestSchema)->InterestSchema:
    updated_interest = session.query(Users_Destinations).filter_by(id=id).first()
    if not updated_interest:
        raise HTTPException(status_code=404, detail=f'The interest with id {id} does not exist')
    for key, value in payload.dict(exclude_unset=True).items():
        setattr(updated_interest, key, value)
    session.commit()
    return updated_interest

# delete a user
@app.delete("/delete/users/{id}")
def delete_user(id: int):
    user = session.query(Users).filter_by(id=id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    session.delete(user)
    session.commit()
    return {"message": f"User with id:{id} deleted successfully"}

#delete a destination
@app.delete("/delete/destinations/{id}")
def delete_destination(id: int):
    destination = session.query(Destinations).filter_by(id=id).first()
    if not destination:
        raise HTTPException(status_code=404, detail="Destination not found")
    session.delete(destination)
    session.commit()
    return {"message": f"Destination with id:{id} deleted successfully"}

#delete an interest
@app.delete('/delete/interest/{id}')
def delete_interest(id:int):
    interest = session.query(Users_Destinations).filter_by(id=id).first()
    if not interest:
        raise HTTPException(status_code=404, detail='Interest not found')
    session.delete(interest)
    session.commit()
    return {'message':f'Interest with id:{id} deleted successfully'}