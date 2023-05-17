from fastapi import APIRouter, Depends, HTTPException
from typing import List

from db.session import Session, get_session
from repositories.metric import MetricRepository
from schemas.metric import MetricCreateBase, MetricCreate, MetricReadBase
from services.metric_handler import MetricHandlerService


router = APIRouter()


@router.post('/metrics', response_model=MetricCreate)
async def add_new_metric(
    metric: MetricCreateBase,
    session: Session = Depends(get_session)
):
    """Added new metric"""
    repo = MetricRepository(session)

    try:
        new_metric = await repo.add_new_metric(metric)
    except Exception:
        raise HTTPException(status_code=500, detail="Creating error")

    return new_metric


@router.get('/metrics/{service_name}', response_model=List[MetricReadBase])
async def get_metrick_by_service_name(
    service_name: str,
    session: Session = Depends(get_session)
):
    """Getting metrics by <service-name>"""
    repo = MetricRepository(session)
    service = MetricHandlerService(repo)

    records = await service.process_metrics(service_name)

    return records
