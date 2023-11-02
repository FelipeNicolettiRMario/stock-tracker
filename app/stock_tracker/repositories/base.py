from stock_tracker.models.base import engine
from sqlalchemy.orm import sessionmaker

class BaseRepo:

    def _get_session(self):
        Session = sessionmaker(bind=engine) 

        return Session()
    