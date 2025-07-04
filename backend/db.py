from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

import config

engine = create_engine(config.DATABASE_URL, echo=config.echo)
SessionLocal = sessionmaker(bind=engine)


class Base(DeclarativeBase):
    pass
