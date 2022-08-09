from pydantic import BaseModel
from datetime import date
from typing import Optional
from decimal import Decimal
from enum import Enum


class OperationKing(str, Enum):
    INCOME = 'income'
    OUTCOME = 'outcome'


class OperationBase(BaseModel):
    date: date
    kind: str
    amount: float
    description: Optional[str]


class Operation(OperationBase):
    id: int

    class Config:
        orm_mode = True


class OperationUpdate(OperationBase):
    pass


class OperationCreate(OperationBase):
    pass
