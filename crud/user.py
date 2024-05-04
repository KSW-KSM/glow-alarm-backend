from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from sqlalchemy import select, update, delete
from models.user import User
from datetime import datetime
import uuid
import time
import random

class CRUDUser:
    @staticmethod
    def insert(db: Session, *, user_name: str, google_id: str, guardian_contact: str, bulb_ip: str, location_id: int):
        max_retries = 5
        for retry in range(max_retries):
            try:
                user_id = str(uuid.uuid4())
                user = User(id=user_id, user_name=user_name, google_id=google_id, guardian_contact=guardian_contact, bulb_ip=bulb_ip, location_id=location_id)
                db.add(user)
                db.commit()
                db.refresh(user)
                return user
            except IntegrityError:
                db.rollback()
                backoff = 2 ** retry + random.uniform(0, 1)  # 지수 백오프
                time.sleep(backoff)
        raise ValueError("User with ID already exists after maximum retries.")

    @staticmethod
    def get(db: Session, id: str):
        return db.get(User, id)

    @staticmethod
    def get_all(db: Session):
        return db.query(User).all()
    
    @staticmethod
    def get_by_google_id(db: Session, google_id: str):
        return db.query(User).filter(User.google_id == google_id).first()

    @staticmethod
    def update(db: Session, *, id: str, user_name: str, google_id: str, guardian_contact: str, bulb_connection: bool, bulb_ip: str):
        # Update the user
        updated_user = db.get(User, id)
        if updated_user:
            updated_at = datetime.now()
            db.query(User).filter(User.id == id).update({"user_name": user_name, "google_id": google_id, "guardian_contact": guardian_contact, "bulb_connection": bulb_connection, "bulb_ip": bulb_ip, "updated_at": updated_at})
            db.commit()
            db.refresh(updated_user)

        return updated_user

    @staticmethod
    def delete(db: Session, id: str):
        deleted_user = db.get(User, id)
        if deleted_user:
            db.delete(deleted_user)
            db.commit()
        return deleted_user


# 싱글톤 객체 생성
crud_user = CRUDUser()
