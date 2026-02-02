from pydantic import BaseModel, EmailStr


class UserSchema(BaseModel):
    name: str
    email: EmailStr


class UserPublicSchema(UserSchema):
    id: int


class UserListPublicSchema(BaseModel):
    users: list[UserPublicSchema]
