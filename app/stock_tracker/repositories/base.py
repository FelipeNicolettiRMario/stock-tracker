from app.stock_tracker.models.base import engine
from sqlalchemy.orm import sessionmaker

class SingletonMeta(type):

    _instance = {}

    def __call__(cls, *args, **kwargs) -> None:
        
        if not cls._instance:

            instance = super().__call__(*args, **kwargs) 
            cls._instance[cls] = instance

        return cls._instance[cls]

class SessionManager(metaclass=SingletonMeta):

    session = None

    def _get_session(self):

        if self.session:
            return self.session
        
        Session = sessionmaker(bind=engine) 
        self.session = Session()

        return self.session
