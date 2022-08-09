from fastapi import APIRouter
from typing import List, Optional

from ..models.operations import (Operation,
                                 OperationKing,
                                 OperationBase,
                                 OperationCreate)

from fastapi import Depends

from ..services.operations import OperationsService

router = APIRouter(
    prefix='/operations',
)


@router.get('/', response_model=List[Operation])
def get_operations(
    kind: Optional[OperationKing] = None,
    service: OperationsService = Depends(),
):
    return service.get_list(kind=kind)


@router.post('/', response_model=List[OperationCreate])
def create_operations(
    operation_data: OperationCreate,
    service: OperationsService = Depends(),
):
    return service.create(operation_data)
