from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

import crud_utils as crud
import models as model
from database import engine, Base, SessionLocal
import jumia_scaper

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/create-users/", response_model=model.User)
async def create_user(user: model.User, db: Session = Depends(get_db)):
    print(f"f{user}")
    db_user = crud.get_user(db, bridge_id=user.bridge_id, authentication_token=user.authentication_token)
    if db_user:
        raise HTTPException(status_code=400, detail="User Credentials Already Exist")
    crud.create_user(db=db, user=user)
    return user


@app.get("/start-jumia-crawler")
async def start_jumia_crawler():
    jumia_scaper.scrape_discount_information_from_jumia()
    return "Success"

