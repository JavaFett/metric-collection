from fastapi import APIRouter

from . import methods


router = APIRouter(prefix='/methods', tags=['methods'])

router.include_router(methods.router)
