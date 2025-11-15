from sqlalchemy import Column, Integer
from sqlalchemy.orm import declarative_base, declared_attr


class CustomBase:
    @declared_attr
    def id(cls):
        return Column(Integer, primary_key=True, index=True)


Base = declarative_base(cls=CustomBase)
