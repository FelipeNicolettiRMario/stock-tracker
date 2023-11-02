from stock_tracker.repositories.rule_repository import IRuleRepository
from stock_tracker.models.rule import Rule

from typing import List
from abc import ABC, abstractmethod

class IRuleService(ABC):
    
    @abstractmethod
    def save_rule(self, rule_data: dict):
        pass

    @abstractmethod
    def get_all_rules(self) -> List[Rule]:
        pass

    @abstractmethod
    def is_rule_satisfied(self, rule:Rule) -> bool:
        pass

class RuleService:

    def __init__(self, repo: IRuleRepository) -> None:
        
        self.__repo = repo

    def save_rule(self, rule_data: dict):
        self.__repo.save_rule(rule_data)

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
