from fastapi import APIRouter
from typing import List, Optional

from ..models.operations import (Operation,
                                 OperationKing,
                                 OperationCreate,
                                 OperationUpdate)

from fastapi import Depends
from fastapi import Response
from fastapi import status

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


@router.post('/', response_model=Operation)
def create_operations(
    operation_data: OperationCreate,
    service: OperationsService = Depends(),
):
    return service.create(operation_data)


@router.get('/{operation_id}', response_model=Operation)
def get_operation(operation_id: int,
                  service: OperationsService = Depends()):
    return service.get(operation_id)


@router.put('/{operation_id}', response_model=Operation)
def update_operation(
        operation_id: int,
        operation_data: OperationUpdate,
        service: OperationsService = Depends()):
    service.update(
        operation_id=operation_id,
        operation_data=operation_data,
    )


@router.delete('/{operation_id}')
def delete_operation(operation_id: int, service: OperationsService = Depends()):
    service.delete(operation_id)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
