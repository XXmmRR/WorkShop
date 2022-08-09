from pydantic import BaseModel
from datetime import date
from typing import Optional
from decimal import Decimal
from enum import Enum


class OperationKing(str, Enum):
    INCOME = 'income'
    OUTCOME = 'outcome'


class Operation(BaseModel):
    id: int
    date: date
    kind: str
    amount: float
    description: Optional[str]

    class Config:
        orm_mode = True
