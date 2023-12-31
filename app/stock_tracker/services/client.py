from app.stock_tracker.models.client import Client
from app.stock_tracker.repositories.client_repository import IClientRepository

from abc import ABC, abstractmethod

class IClientService(ABC):

    @abstractmethod
    def add_client(self, client_data: dict) -> Client:
        pass

class ClientService(IClientService):

    def __init__(self, repo: IClientRepository) -> None:
        self.__repo = repo

    def add_client(self, client_data: dict):
        return self.__repo.save_client(client_data)

