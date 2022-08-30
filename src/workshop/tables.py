import sqlalchemy as sq
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Operation(Base):
    __tablename__ = 'operations'
    id = sq.Column(sq.Integer, primary_key=True)
    user_id = sq.Column(sq.Integer, sq.ForeignKey('users.id'))
    date = sq.Column(sq.Date)
    kind = sq.Column(sq.String)
    amount = sq.Column(sq.Numeric(10, 2))
    description = sq.Column(sq.String, nullable=True)


class User(Base):
    __tablename__ = 'users'
    id = sq.Column(sq.Integer, primary_key=True)
    email = sq.Column(sq.Text, unique=True)
    username = sq.Column(sq.Text, unique=True)
    password_hash = sq.Column(sq.Text)
