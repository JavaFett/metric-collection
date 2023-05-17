from schemas.base import BaseSchema


class MetricCreateBase(BaseSchema):
    service_name: str
    path: str
    response_time_ms: str


class MetricCreate(MetricCreateBase):
    id: int

    class Config:
        orm_mode = True


class MetricReadBase(BaseSchema):
    path: str
    average: str
    min: str
    max: str
    p99: str | None
