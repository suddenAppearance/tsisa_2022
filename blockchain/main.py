import sys

from alembic.config import Config
from fastapi import FastAPI

from alembic import command
from api.api import router
from models.base import create_session

app = FastAPI(title="Blockchain")


@app.get("/")
async def status():
    with create_session() as session:
        session.execute('SELECT 1')

    return {'status': 'ok'}


app.include_router(router, prefix="/api")

config = Config(stdout=sys.stderr)
config.set_main_option("script_location", "alembic")
command.upgrade(config, 'head')
