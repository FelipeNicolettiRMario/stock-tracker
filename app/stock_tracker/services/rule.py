from stock_tracker.repositories.rule_repository import IRuleRepository
from stock_tracker.models.rule import Rule

from typing import List


class RuleService:

    def __init__(self, repo: IRuleRepository) -> None:
        
        self.__repo = repo

    def save_rule(self, rule_data: dict):
        self.__repo.save_rule(rule_data)

    def get_all_rules(self) -> List[Rule]:
        self.__repo.get_all_rules()
    
