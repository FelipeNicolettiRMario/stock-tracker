from app.stock_tracker.models.rule import Rule
from app.stock_tracker.gateway.finance import IFinanceGateway
from .base import BaseRepo

from typing import List
from abc import ABC, abstractmethod
from sqlalchemy import select

class IRuleRepository(ABC):

    @abstractmethod
    def save_rule(self, rule_data: dict):
        pass

    @abstractmethod
    def get_all_rules(self) -> List[Rule]:
        pass

    @abstractmethod
    def get_rule_ticker_actual_value(self, rule: Rule) -> float:
        pass

class RuleRepository(BaseRepo, IRuleRepository):

    def __init__(self, finance_gateway: IFinanceGateway) -> None:
        super(BaseRepo).__init__()
        self.__sesion = self._get_session()
        self.__finance_gateway = finance_gateway

    def save_rule(self, rule_data: dict):
        
        rule = Rule.from_dict(rule_data)
        self.__sesion.add(rule)
        self.__sesion.commit()
    
    def get_all_rules(self):
        
        query = select(Rule).limit(100)

        return self.__sesion.execute(query).all()
    
    def get_rule_ticker_actual_value(self, rule: Rule) -> float:

        return self.__finance_gateway.get_most_recent_price(rule.ticker)