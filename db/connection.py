from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DB_URL = "mysql+pymysql://root:password@127.0.0.1:3306/soundlight"
SQLALCHEMY_DB_URL = "mysql+pymysql://root:soundlight1234!@127.0.0.1:3306/soundlight"
# SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root:root@db:3306/dev_db"

engine = create_engine(
    SQLALCHEMY_DB_URL,
    # connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
