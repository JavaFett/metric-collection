from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from settings import settings


engine = create_engine(settings.DATABASE_URL, connect_args={
    "check_same_thread": False})


Session = sessionmaker(
    autocommit=False, autoflush=False, bind=engine)


def get_session():
    session = Session()
    try:
        yield session
    finally:
        session.close()


Base = declarative_base()
