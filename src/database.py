from sqlalchemy.orm import sessionmaker, DeclarativeBase
from sqlalchemy import URL, create_engine, text
from src.config import settings

engine = create_engine(
    url=settings.DATABASE_URL_sqlite,
    echo=True,
)

Session = sessionmaker(engine)


class Base(DeclarativeBase):
    pass
