from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from conf.settings.base import DATABASE

# Database configuration
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{DATABASE['USERNAME']}:{DATABASE['PASSWORD']}@{DATABASE['HOST']}:{DATABASE['PORT']}/{DATABASE['NAME']}"

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Dependency to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
