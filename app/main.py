import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import api
from db.session import engine, Base
from settings import settings


Base.metadata.create_all(bind=engine)


app = FastAPI(
    title='metric-collection-service',
    description='Metric collection service',
    version='0.1.0',
    debug=settings.DEBUG
)

app.include_router(api.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


if __name__ == '__main__':
    uvicorn.run(
        'main:app',
        port=settings.SERVER_PORT,
        host=settings.SERVER_HOST,
        reload=settings.SERVER_RELOAD
    )
