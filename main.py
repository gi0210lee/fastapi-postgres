from fastapi import FastAPI, Depends, HTTPException
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from schema import User
import crud, models, schema

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

def db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/")        
def default():
    return  {"hello":"world!!"}


# @app.get("/user", response_model=schema.UserList)
@app.get("/user")
def user_list(db: Session = Depends(db), user_find: str = ''):
    user_list = crud.get_user_list(db, user_find)
    # if user is None:
    #     raise HTTPException(404, crud.error_message('Not Found'))        
    # return {"user_list": user_list}
    return user_list
        

# @app.post('/user/create', response_model=schema.User)
@app.post('/user/create')
def user_create(user_create: schema.UserCreate, db: Session = Depends(db)):
    user_list = crud.get_user_list(db, user_find=user_create.name)
    if user_list:
        print('user_list=', user_list)
        raise HTTPException(400, crud.error_message('Already Exists'))
    return crud.create_user(db, user_create)