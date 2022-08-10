from sqladmin import ModelView
from .tables import Operation


class UserAdmin(ModelView, model=Operation):
    column_list = [Operation.id, Operation.date, Operation.kind, Operation.amount, Operation.description]


