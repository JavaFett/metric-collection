from functools import lru_cache
from itertools import groupby
from operator import attrgetter

from typing import List
import numpy

from repositories.metric import MetricRepository
from schemas.metric import MetricReadBase


class MetricHandlerService:
    def __init__(self, repository: MetricRepository) -> None:
        self.repository = repository

    async def process_metrics(self, service_name: str) -> List[MetricReadBase]:
        metrics = await self.repository.get_metrics_by_service_name(service_name)
        result = []
        grouped_metrics = [(key, list(group)) for key, group in groupby(
            metrics, attrgetter('path'))]

        for item in grouped_metrics:
            values = {}
            path = item[0]
            response_time_list = [el.response_time_ms for el in item[1]]

            values['path'] = path
            values['average'] = round(
                sum(response_time_list) / len(response_time_list))
            values['min'] = min(response_time_list)
            values['max'] = max(response_time_list)
            values['p99'] = round(numpy.percentile(response_time_list, 99))

            result.append(MetricReadBase(**values))

        return result
