from fastapi import APIRouter, Depends, HTTPException, Path, Body
from fastapi.responses import Response, JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List
from sqlalchemy.orm import Session
from api.depends.get_db import get_db
from crud.alarm import crud_alarm
from schemas.alarm import AlarmCreate, AlarmUpdate, AlarmInDB, AlarmResponse

router = APIRouter()

@router.post("/alarm", response_model=AlarmResponse)
def create_alarm(alarm: AlarmCreate, db: Session = Depends(get_db)):
    try:
        created_alarm = crud_alarm.insert(db=db, alarm_time=alarm.alarm_time, repeat_day=alarm.repeat_day, light_color=alarm.light_color, alarm_status=alarm.alarm_status, user_id=alarm.user_id)
    except Exception as e:
        raise HTTPException(status_code=404, detail=f"Alarm creation failed: {str(e)}")

    return JSONResponse(status_code=201, content=jsonable_encoder(created_alarm))

@router.get("/alarm/{id}", response_model=AlarmResponse)
def read_alarm(id: str = Path(..., min_length=1), db: Session = Depends(get_db)):
    try:
        alarm = crud_alarm.get(db, id)
    except:
        raise HTTPException(status_code=422, detail="Validation error")
    if not alarm:
        raise HTTPException(status_code=404, detail="Alarm not found")
    return JSONResponse(status_code=200, content=jsonable_encoder(alarm))

@router.get("/alarms/user/{user_id}", response_model=List[AlarmResponse])
def read_alarms_by_user_id(user_id: str = Path(..., min_length=1), db: Session = Depends(get_db)):
    alarms = crud_alarm.get_all_by_user_id(db, user_id)
    return JSONResponse(status_code=200, content=jsonable_encoder(alarms))

@router.get("/alarms", response_model=List[AlarmInDB])
def read_alarms(db: Session = Depends(get_db)):
    alarms = crud_alarm.get_all(db)
    return JSONResponse(status_code=200, content=jsonable_encoder(alarms))

@router.put("/alarm/{id}", response_model=AlarmResponse)
def update_alarm(id: str = Path(..., min_length=1), db: Session = Depends(get_db),
                 alarm: AlarmUpdate = Body(...)):
    try:
        updated_alarm = crud_alarm.update(db=db, id=id, alarm_time=alarm.alarm_time, repeat_day=alarm.repeat_day, light_color=alarm.light_color, alarm_status=alarm.alarm_status, user_id=alarm.user_id)
    except:
        raise HTTPException(status_code=422, detail="Validation error")
    if not updated_alarm:
        raise HTTPException(status_code=404, detail="Alarm not found")
    return JSONResponse(status_code=200, content=jsonable_encoder(updated_alarm))

@router.delete("/alarm/{id}", response_model=None)
def delete_alarm(id: str = Path(..., min_length=1), db: Session = Depends(get_db)):
    deleted_alarm = crud_alarm.delete(db, id)
    if not deleted_alarm:
        raise HTTPException(status_code=404, detail="Alarm not found")
    return Response(status_code=204)
