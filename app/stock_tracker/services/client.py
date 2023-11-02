from stock_tracker.models.client import Client
from stock_tracker.repositories.client_repository import IClientRepository

class ClientService:

    def __init__(self, repo: IClientRepository) -> None:
        self.__repo = repo

    def add_client(self, client_data: dict):
        self.__repo.save_client(client_data)

