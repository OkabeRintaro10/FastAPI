from sqlalchemy import create_engine
from conf.settings.base import DATABASE
from .models import Base

Base.metadata.create_all(
    bind=create_engine(
        f"mysql+pymysql://{DATABASE['USERNAME']}:{DATABASE['PASSWORD']}@172.18.0.2:{DATABASE['PORT']}/{DATABASE['NAME']}",
        pool_pre_ping=True,
        echo=True,
    )
)
