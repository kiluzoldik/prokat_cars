from sqlalchemy import text, insert, inspect, select, desc
from sqlalchemy.orm import selectinload
from src.database import engine, Session, Base
from src.models import Person, Order
from datetime import datetime


@staticmethod
def create_tables():
    engine.echo = False
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    engine.echo = False


@staticmethod
def insert_persons(name, email, phone):
    with Session() as sess:

        res = Person(full_name=name,
                     email=email,
                     phone_number=phone,
                     )
        sess.add(res)
        sess.commit()


@staticmethod
def insert_orders(mark_, model_, place_in_, place_out_, date_in_, date_out_, comments_):
    with Session() as sess:
        res = sess.query(Person.id).order_by(desc(Person.id)).first()[0]
        result = Order(mark=mark_,
                       modal=model_,
                       place_in=place_in_,
                       place_out=place_out_,
                       date_in=date_in_,
                       date_out=date_out_,
                       comment=comments_,
                       person_id=res,
                       )
        sess.add(result)
        sess.commit()
