from app.core.settings import POSTGRESS_URL
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


connection_string = POSTGRESS_URL
engine = create_engine(connection_string, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

