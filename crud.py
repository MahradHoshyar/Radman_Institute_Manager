from sqlalchemy import select
from sqlalchemy.orm import Session
import models
from models import engine
import schemas


# add all operations for object of user:
# create_user, get_user , get_user_by_last_name , get_users , update_user and delete_user_by_id
# -------------------------------------------------------------------------------------------------------

def create_user(db: Session(engine), user: schemas.UserCreate):
    db_user = models.User(id=user.id, gender=user.gender, first_name=user.first_name, last_name=user.last_name,
                          father_name=user.father_name, date_of_birth=user.date_of_birth,
                          national_code=user.national_code, phone_number=user.phone_number, role_id=user.role_id,
                          recruitment_date=user.recruitment_date, is_super_admin=user.is_super_admin,
                          is_panel_user=user.is_panel_user, permission_group_id=user.permission_group_id,
                          is_enabled=user.is_enabled, recorder_id=user.recorder_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_user(db: Session(engine), user_id: int):
    db_user = db.scalars(select(models.User).where(models.User.id == user_id))
    if not [*db_user]:
        return None
    return db.scalars(select(models.User).where(models.User.id == user_id)).one()


def get_user_by_last_name(db: Session(engine), user_last_name: str):
    db_user = db.scalars(select(models.User).where(models.User.last_name == user_last_name))
    if not [*db_user]:
        return None
    return db.scalars(select(models.User).where(models.User.last_name == user_last_name)).one()


def get_users(db: Session(engine)):
    return db.scalars(select(models.User))


def update_user(db: Session(engine), user: schemas.User):
    db_user = db.scalars(select(models.User).where(models.User.id == user.id)).one()
    db_user.id = user.id
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
    db_user = db.get(models.User, user_id)
    db.delete(db_user)
    db.commit()
    return db_user
