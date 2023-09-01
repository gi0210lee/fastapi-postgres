from sqlalchemy.orm import Session
import schema, models

def create_user(db: Session, user_create: schema.UserCreate):
    user = models.User(name=user_create.name)
    db.add(user)
    db.commit()
    db.refresh(user)
    return user

def get_user_list(db: Session, user_find: str = ''):    
    user_list = db.query(models.User)    
    if user_list and user_find:
        user_list = user_list.filter(models.User.name == user_find)
    return user_list.all()

def error_message(message):
    return {
        'error': message
    }