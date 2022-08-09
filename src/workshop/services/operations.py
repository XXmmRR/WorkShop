from .. import tables
from ..database import get_session
from ..models.operations import OperationKing, OperationCreate
from fastapi import Depends
from sqlalchemy.orm import Session

from typing import (List,
                    Optional)


class OperationsService:
    def __init__(self, session: Session = Depends(get_session),
                 ):
        self.session = session

    def get_list(self,  kind: Optional[OperationKing] = None,) -> List[tables.Operation]:
        query = self.session.query(tables.Operation)
        if kind:
            query = query.filter_by(kind=kind)
        operations = query.all()
        return operations

    def create(self, operation_data: OperationCreate) -> tables.Operation:
        operation = tables.Operation(**operation_data.dict())
        self.session.add(operation)
        self.session.commit()
        return operation
