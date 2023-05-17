from sqlalchemy import select, func
from typing import List

from db.session import Session
from models.metric import Metric
from schemas.metric import MetricCreateBase


class MetricRepository:
    def __init__(self, session: Session) -> None:
        self.session = session

    async def add_new_metric(self, metric: MetricCreateBase) -> Metric:
        metric = Metric(**metric.dict())

        self.session.add(metric)
        self.session.commit()

        return metric

    async def get_metrics_by_service_name(self, service_name: str) -> List[Metric]:
        #     records = self.session.execute(
        #         select(Metric.path, func.avg(Metric.response_time_ms),
        #                func.min(Metric.response_time_ms), func.max(
        #                    Metric.response_time_ms))
        #         .where(Metric.service_name == service_name)
        #         .group_by(Metric.path)
        #     ).all()

        metrics = self.session.query(Metric).filter_by(
            service_name=service_name).order_by().order_by(Metric.path).all()

        return metrics
