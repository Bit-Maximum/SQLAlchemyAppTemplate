from sqlalchemy.orm import sessionmaker
from database.database_setup import Engine

Session = sessionmaker(bind=Engine)
