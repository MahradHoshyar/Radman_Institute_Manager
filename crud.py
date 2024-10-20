from sqlalchemy import select
from sqlalchemy.orm import Session
import models
from models import engine
import schemas


# add all operations for object of user:
# create_user, get_user , get_user_by_last_name , get_users , update_user and delete_user_by_id
# -------------------------------------------------------------------------------------------------------

def create_user(db: Session(engine), user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session(engine), user_id: int):
    return db.scalars(select(models.User).where(models.User.id == user_id, models.User.is_enabled)).first()


def get_user_by_last_name(db: Session(engine), user_last_name: str):
    return db.scalars(select(models.User).where(models.User.last_name == user_last_name,
                                                models.User.is_enabled)).first()


def get_users(db: Session(engine)):
    return db.scalars(select(models.User).where(models.User.is_enabled))


def update_user(db: Session(engine), user: schemas.User, user_id: int):
    db_user = db.scalars(select(models.User).where(models.User.id == user_id)).first()
    db_user.gender = user.gender
    db_user.first_name = user.first_name
    db_user.last_name = user.last_name
    db_user.father_name = user.father_name
    db_user.date_of_birth = user.date_of_birth
    db_user.national_code = user.national_code
    db_user.phone_number = user.phone_number
    db_user.role_id = user.role_id
    db_user.recruitment_date = user.recruitment_date
    db_user.is_super_admin = user.is_super_admin
    db_user.is_panel_user = user.is_panel_user
    db_user.permission_group_id = user.permission_group_id
    db_user.is_enabled = user.is_enabled
    db_user.recorder_id = user.recorder_id
    db.commit()
    return db_user


def delete_user_by_id(db: Session(engine), user_id: int):
    db_user = db.scalars(select(models.User).where(models.User.id == user_id)).one()
    db_user.is_enabled = False
    db.commit()
    return db_user
