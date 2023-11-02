from .base import BaseRepo
from app.stock_tracker.models.client import Client

from sqlalchemy import select
from abc import ABC, abstractmethod

class IClientRepository(ABC):

    @abstractmethod
    def save_client(self, client_data: dict):
        """
            `client_data` = Client data that will be used for create a Client
        """
        pass

class ClientSQLRepository(BaseRepo,IClientRepository):

    def __init__(self) -> None:
        super(BaseRepo).__init__()
        self.__session = self._get_session()

    def _get_client_by_parameter(self, parameter_name: str, parameter: str) -> Client | None:
        """
         `parameter_name` = Parameter tha will be used for search clien, must be email or phone
         `parameter` = Parameter value that will be used in the query
        """
        parameter_name = parameter_name.lower()
        query_by_parameter = {
            "email":select(Client).where(Client.email == parameter),
            "phone":select(Client).where(Client.phone == parameter)
        }

        query = query_by_parameter.get(parameter_name)
        
        return self.__session.execute(query).one_or_none()
    
    def _update_client(self,client: Client, client_data: dict):

        client.update(client_data)
        self.__session.commit()
        self.__session.flush()


    def save_client(self, client_data: dict):
        
        email = client_data.get("email")
        phone = client_data.get("phone")

        client = None
        if email:
            client = self._get_client_by_parameter("email", email)
        elif phone:
            client = self._get_client_by_parameter("phone", phone)
        else:
            raise ValueError("Client must have email or phone")

        if client:
            self._update_client(client, client_data)

        else:
            client = Client.from_dict(client_data)
            self.__session.add(client)
            self.__session.commit()