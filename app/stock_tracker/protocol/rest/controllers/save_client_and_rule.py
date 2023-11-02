from stock_tracker.protocol.rest.models.aggregates import AggregateClientAndRule

from stock_tracker.services.factory import ServiceFactory

def save_client_and_rule_controller(aggregated: AggregateClientAndRule):
        
    client_service = ServiceFactory.get_client_service()
    rule_service = ServiceFactory.get_rule_service()

    client_service.add_client(aggregated.client.model_dump())
    rule_service.save_rule(aggregated.rule.model_dump())