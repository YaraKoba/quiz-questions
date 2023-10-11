from app.core.settings import POSTGRESS_URI
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


connection_string = POSTGRESS_URI
engine = create_engine(connection_string, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

