from contextlib import asynccontextmanager
from fastapi import FastAPI

from api.v1.routes import user_routes
from database.setup import create_db_and_tables, engine


@asynccontextmanager
async def lifespan(server: FastAPI):
    print("Creating database and tables")
    create_db_and_tables()
    yield
    print("Disposing engine")
    engine.dispose()


server = FastAPI(
    title="User Management Service",
    version="1.0.0", 
    lifespan=lifespan
)

server.include_router(user_routes.router)
