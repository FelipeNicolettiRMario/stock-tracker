from app.stock_tracker.models.rule import Rule
from app.stock_tracker.models.client import Client
from app.stock_tracker.gateway.finance import IFinanceGateway
from .base import SessionManager

from typing import List
from abc import ABC, abstractmethod
from sqlalchemy import select

class IRuleRepository(ABC):

    @abstractmethod
    def save_rule(self, rule_data: dict) -> Rule:
        pass

    @abstractmethod
    def get_all_rules(self) -> List[Rule]:
        pass

    @abstractmethod
    def get_rule_ticker_actual_value(self, rule: Rule) -> float:
        pass

    @abstractmethod
    def add_client_to_rule(self, rule: Rule, client: Client):
        pass

    @abstractmethod
    def get_single_rule(self, rule_id: int) -> Rule:
        pass

class RuleRepository(IRuleRepository):

    def __init__(self, finance_gateway: IFinanceGateway) -> None:
        super().__init__()
        self.__session = SessionManager()._get_session()
        self.__finance_gateway = finance_gateway

    def save_rule(self, rule_data: dict):
        
        rule = Rule.from_dict(rule_data)
        self.__session.add(rule)
        self.__session.commit()
        return rule
    
    def get_all_rules(self):
        
        query = select(Rule).limit(100)

        return self.__session.execute(query).all()
    
    def get_rule_ticker_actual_value(self, rule: Rule) -> float:

        return self.__finance_gateway.get_most_recent_price(rule.ticker)
    
    def add_client_to_rule(self, rule: Rule, client: Client):
        rule.clients.append(client)
        self.__session.commit()
        self.__session.flush()

    def get_single_rule(self, rule_id: int) -> Rule:
        return Rule.get(rule_id)