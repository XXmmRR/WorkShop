from fastapi import APIRouter
from typing import List
from ..models.operations import Operation
from .. import tables
from ..database import Session

router = APIRouter(
    prefix='/operations',
)


@router.get('/', response_model=List[Operation])
def get_operations():
    session = Session()
    operations = (
        session
        .query(tables.Operation)
        .all()
    )
    return operations
