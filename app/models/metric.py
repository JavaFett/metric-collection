from sqlalchemy import Column, Integer, String

from db.session import Base


class Metric(Base):
    __tablename__ = 'metrics'

    id = Column(Integer, primary_key=True, unique=True)
    service_name = Column(String)
    path = Column(String)
    response_time_ms = Column(Integer)
