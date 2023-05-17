from fastapi import APIRouter

from . import rest


router = APIRouter(prefix='/rest')

router.include_router(rest.router)
