from pydantic import BaseModel


class UserCreateSchema(BaseModel):
    username: str


class UserUpdateBalanceSchema(BaseModel):
    balance_change: float