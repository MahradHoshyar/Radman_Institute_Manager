from fastapi import Depends, FastAPI, HTTPException
import crud
import models
import schemas
from models import SessionLocal, engine
from sqlalchemy.orm import Session
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# Endpoints of users
# add all Endpoints for user
# -------------------------------------------------------------------------------------------------------

@app.post("/users/create", response_model=schemas.User)
async def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
async def read_users(db: Session = Depends(get_db)):
    users = crud.get_users(db)
    if not [*users]:
        raise HTTPException(status_code=404, detail="user not found")
    return users


@app.get("/users/{user_id}", response_model=None)
async def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="user not found")
    return db_user


@app.get("/users/read_user_by_last_name/{user_last_name}")
async def read_user_by_last_name(user_last_name: str, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_last_name(db=db, user_last_name=user_last_name)
    if db_user is None:
        raise HTTPException(status_code=404, detail="user not found")
    return db_user


@app.put("/users/update/{user_id}", response_model=schemas.User)
async def update_user(user: schemas.UserUpdate, user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="user not found!")
    return crud.update_user(db=db, user=user, user_id=user_id)


@app.delete("/users/delete/{user_id}")
async def delete_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user:
        crud.delete_user_by_id(db=db, user_id=user_id)
        return {"massage": f"user with id: {user_id} successfully deleted"}
    else:
        raise HTTPException(status_code=404, detail="user not found!")
