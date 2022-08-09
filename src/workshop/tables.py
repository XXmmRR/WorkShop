import sqlalchemy as sq
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Operation(Base):
    __tablename__ = 'operations'
    id = sq.Column(sq.Integer, primary_key=True)
    date = sq.Column(sq.Date)
    kind = sq.Column(sq.String)
    amount = sq.Column(sq.Numeric(10, 2))
    description = sq.Column(sq.String, nullable=True)