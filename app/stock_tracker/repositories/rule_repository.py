from stock_tracker.models.rule import Rule
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

class RuleSQLRepository(BaseRepo, IRuleRepository):

    def __init__(self) -> None:
        super(BaseRepo).__init__()
        self.__sesion = self._get_session()

    def save_rule(self, rule_data: dict):
        
        rule = Rule.from_dict(rule_data)
        self.__sesion.add(rule)
        self.__sesion.commit()
    
    def get_all_rules(self):
        
        query = select(Rule).limit(100)

        return self.__sesion.execute(query).all()
    