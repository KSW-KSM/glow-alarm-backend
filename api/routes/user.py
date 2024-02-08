import logging
from fastapi import APIRouter, Depends, HTTPException, Path, Body
from fastapi.responses import Response, JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
from sqlalchemy.orm import Session
from api.depends.get_db import get_db
from crud.user import crud_user
from schemas.user import UserCreate, UserUpdate, UserInDB

router = APIRouter()

@router.post("/user", response_model=UserInDB)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    try:
        created_user = crud_user.insert(db=db, id=user.id, user_name=user.user_name, google_id=user.google_id, guardian_contact=user.guardian_contact, bulb_ip=user.bulb_ip, value=user.value)
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"User creation failed: {str(e)}")

    return JSONResponse(status_code=201, content=jsonable_encoder(created_user))

@router.get("/user/{id}", response_model=UserInDB)
def read_user(id: str = Path(..., min_length=1), db: Session = Depends(get_db)):
    try:
        user = crud_user.get(db, id)
    except:
        raise HTTPException(status_code=422, detail="Validation error")
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return JSONResponse(status_code=200, content=jsonable_encoder(user))

@router.get("/users", response_model=List[UserInDB])
def read_users(db: Session = Depends(get_db)):
    users = crud_user.get_all(db)
    return JSONResponse(status_code=200, content=jsonable_encoder(users))

@router.put("/user/{id}", response_model=UserInDB)
def update_user(id: str = Path(..., min_length=1), db: Session = Depends(get_db),
                 user: UserUpdate = Body(...)):
    try:
        updated_user = crud_user.update(db=db, id=id, user_name=user.user_name, google_id=user.google_id, guardian_contact=user.guardian_contact, bulb_connection=user.bulb_connection, bulb_ip=user.bulb_ip, value=user.value)
    except:
        raise HTTPException(status_code=422, detail="Validation error")
    if not updated_user:
        raise HTTPException(status_code=404, detail="User not found")
    return JSONResponse(status_code=200, content=jsonable_encoder(updated_user))

@router.delete("/user/{id}", response_model=None)
def delete_user(id: str = Path(..., min_length=1), db: Session = Depends(get_db)):
    deleted_user = crud_user.delete(db, id)
    if not deleted_user:
        raise HTTPException(status_code=404, detail="User not found")
    return Response(status_code=204)
