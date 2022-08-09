import sqlalchemy as sq
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Operation(Base):
    __tablename__ = 'operations'
    id = sq.Column(sq.Integer, primary_key=True)
    data = sq.Column(sq.Date)
    amount = sq.Column(sq.Numeric(10, 2))
    description = sq.Column(sq.String, nullable=True)
