from typing import Annotated, List
from fastapi import APIRouter, HTTPException, Query, status
from sqlmodel import select
from helpers.functions.generate_response_messages import generate_multiple_response_messages
from models.user_model import User

from api.v1.schemas.user_schema import UserCreate, UserRead, UserUpdate
from database.setup import SessionDep


responses = {
    404: "No data found",
    400: "Something is wrong with the payload you've sent",
    500: "Something went wrong with the server, consider trying later",
}

common_props = {
    "responses": generate_multiple_response_messages(responses)
}

NO_USER_FOUND = "No user found with that id"

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("", response_model=List[UserRead], status_code=status.HTTP_200_OK, **common_props)
def read_users(session: SessionDep, offset: int = 0, limit: Annotated[int, Query(le=100)] = 100):
    statement = select(User).offset(offset).limit(limit)
    users = session.exec(statement).all()

    return users


@router.get("/user/{user_id}", response_model=UserRead, status_code=status.HTTP_200_OK, **common_props)
def read_one_user(session: SessionDep, user_id: int):
    user = session.get(User, user_id)

    if not user:
        raise HTTPException(
            status_code=404, detail={
                "message": NO_USER_FOUND}
        )

    return user


@router.post("/create", response_model=UserRead, status_code=status.HTTP_201_CREATED, **common_props)
def create_user(session: SessionDep, payload: UserCreate):
    new_user = User(**payload.model_dump())

    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return new_user


@router.put("/update/{user_id}", response_model=UserRead, status_code=status.HTTP_200_OK, **common_props)
def update_user(session: SessionDep, user_id: int, payload: UserUpdate):
    user = session.get(User, user_id)

    if not user:
        raise HTTPException(
            status_code=404, detail={
                "message": NO_USER_FOUND}
        )

    for key, value in payload.model_dump(exclude_unset=True).items():
        setattr(user, key, value)

    session.commit()
    session.refresh(user)

    return user


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT, **common_props)
def remove_user(session: SessionDep, user_id: int):
    user = session.get(User, user_id)

    if not user:
        raise HTTPException(
            status_code=404, detail={
                "message": NO_USER_FOUND}
        )

    session.delete(user)
    session.commit()
