from .client import IClientService
from .rule import IRuleService

class ServiceFactory:

    @staticmethod
    def get_client_service() -> IClientService:

        from stock_tracker.repositories.client_repository import ClientSQLRepository
        from stock_tracker.services.client import ClientService

        return ClientService(ClientSQLRepository())
    
    @staticmethod
    def get_rule_service() -> IRuleService:

        from stock_tracker.repositories.rule_repository import RuleRepository
        from stock_tracker.services.rule import RuleService
        from stock_tracker.gateway.yahoo_finance import YahooFinanceGateway

        return RuleService(
            RuleRepository(
                YahooFinanceGateway()
            )
        )