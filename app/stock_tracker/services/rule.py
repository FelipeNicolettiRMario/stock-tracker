from app.stock_tracker.repositories.rule_repository import IRuleRepository
from app.stock_tracker.models.rule import Rule
from app.stock_tracker.models.client import Client

from typing import List
from abc import ABC, abstractmethod

class IRuleService(ABC):
    
    @abstractmethod
    def save_rule(self, rule_data: dict) -> Rule:
        pass

    @abstractmethod
    def get_all_rules(self) -> List[Rule]:
        pass

    @abstractmethod
    def is_rule_satisfied(self, rule:Rule) -> bool:
        pass

    @abstractmethod
    def add_client_to_rule(self, rule: Rule, client: Client):
        pass
    
class RuleService:

    def __init__(self, repo: IRuleRepository) -> None:
        
        self.__repo = repo

    def save_rule(self, rule_data: dict) -> Rule:
        return self.__repo.save_rule(rule_data)

    def get_all_rules(self) -> List[Rule]:
        self.__repo.get_all_rules()
    
    def _is_targe_operation_rule_satisfied(self, rule: Rule) -> bool:

        ticker_actual_value = self.__repo.get_rule_ticker_actual_value(rule.ticker)

        if rule.operator:
            return ticker_actual_value > rule.target
        
        else:
            return ticker_actual_value < rule.target

    def _is_comparison_operation_rule_satisfied(self, rule: Rule) -> bool:

        comparision_target_actual_value = self.__repo.get_rule_ticker_actual_value(rule.comparison_target)
        ticker_actual_value = self.__repo.get_rule_ticker_actual_value(rule.ticker)

        if rule.operator:
            return ticker_actual_value > comparision_target_actual_value
        else:
            return ticker_actual_value < comparision_target_actual_value

    def is_rule_satisfied(self, rule:Rule) -> bool:

        if not rule.comparison_target:
            return self._is_targe_operation_rule_satisfied(rule)
        
        return self._is_comparison_operation_rule_satisfied(rule)

    def add_client_to_rule(self, rule: Rule, client: Client):
        self.__repo.add_client_to_rule(rule, client)
