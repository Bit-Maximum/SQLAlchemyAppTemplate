from sqlalchemy.engine import create_engine
from sqlalchemy.orm import declarative_base

import settings


Engine = create_engine(settings.DATABASE_URL, echo=True)
Base = declarative_base()
