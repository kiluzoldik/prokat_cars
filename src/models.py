from typing import Optional, Annotated
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey
from src.database import Base
from datetime import datetime

intpk = Annotated[int, mapped_column(primary_key=True)]
unique = Annotated[str, mapped_column(unique=True)]


class Person(Base):
    __tablename__ = "persons"

    id: Mapped[intpk]
    full_name: Mapped[str]
    email: Mapped[unique]
    phone_number: Mapped[unique]
    order: Mapped["Order"] = relationship(back_populates="person")


class Order(Base):
    __tablename__ = 'orders'

    id: Mapped[intpk]
    mark: Mapped[str]
    modal: Mapped[str]
    place_in: Mapped[str]
    place_out: Mapped[str]
    date_in: Mapped[str]
    date_out: Mapped[str]
    comment: Mapped[Optional[str]]
    person_id: Mapped[int] = mapped_column(ForeignKey("persons.id"))
    person: Mapped["Person"] = relationship(back_populates="order")
