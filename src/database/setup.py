from typing import Annotated
from fastapi import Depends
from sqlmodel import SQLModel, Session, create_engine


sql_db_name = "users_management.db"
sql_url = f"sqlite:///{sql_db_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sql_url, echo=True, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
