from fastapi import APIRouter, status

from app.db import USER
from app.schemas.users import (
    UserListPublicSchema,
    UserSchema,
    UserPublicSchema,
)

router = APIRouter()


@router.post(
    path="/",
    status_code=status.HTTP_201_CREATED,
    response_model=UserPublicSchema,
)
async def create_user(user: UserSchema):
    user_with_id = UserPublicSchema(
        **user.model_dump(),
        id=len(USER) + 1,
    )
    USER.append(user_with_id)
    return user_with_id


@router.get(
    path="/",
    status_code=status.HTTP_200_OK,
    response_model=UserListPublicSchema,
)
async def list_users():
    return {"users": USER}
