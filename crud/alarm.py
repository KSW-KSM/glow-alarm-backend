from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from models.alarm import Alarm
from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
from pytz import utc
import uuid

scheduler = BackgroundScheduler(timezone=utc)

class CRUDAlarm:
    def insert(db: Session, *, alarm_time: datetime, name: str, repeat_day: list, light_color: str, alarm_status: bool, user_id: int):
        while True:
            try:
                alarm_id = str(uuid.uuid4())
                repeat_day_str = ','.join(repeat_day)
                alarm = Alarm(id=alarm_id, alarm_time=alarm_time, name=name, repeat_day=repeat_day_str, light_color=light_color, alarm_status=alarm_status, user_id=user_id)
                db.add(alarm)
                db.commit()
                db.refresh(alarm)
                return alarm
            except IntegrityError:
                db.rollback()
                continue

    @staticmethod
    def get(db: Session, id: int):
        return db.get(Alarm, id)

    @staticmethod
    def get_all(db: Session):
        return db.query(Alarm).all()
    
    @staticmethod
    def get_all_by_user_id(db: Session, user_id: int):
        return db.query(Alarm).filter(Alarm.user_id == user_id).all()

    @staticmethod
    def update(db: Session, *, id: str, alarm_time: datetime, repeat_day: list, light_color: str, alarm_status: bool, user_id: int):
        repeat_day_str = ','.join(repeat_day)
        updated_alarm = db.get(Alarm, id)
        if updated_alarm:
            updated_at = datetime.now()
            db.query(Alarm).filter(Alarm.id == id).update({"alarm_time": alarm_time, "repeat_day": repeat_day_str, "light_color": light_color, "alarm_status": alarm_status, "user_id": user_id, "updated_at": updated_at})
            db.commit()
            db.refresh(updated_alarm)

        return updated_alarm

    @staticmethod
    def delete(db: Session, id: int):
        deleted_alarm = db.get(Alarm, id)
        if deleted_alarm:
            db.delete(deleted_alarm)
            db.commit()
        return deleted_alarm



# 싱글톤 객체 생성
crud_alarm = CRUDAlarm()
