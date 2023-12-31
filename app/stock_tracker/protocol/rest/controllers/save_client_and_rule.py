from app.stock_tracker.protocol.rest.models.aggregates import AggregateClientAndRule

from app.stock_tracker.services.factory import ServiceFactory

def save_client_and_rule_controller(aggregated: AggregateClientAndRule):
        
    client_service = ServiceFactory.get_client_service()
    rule_service = ServiceFactory.get_rule_service()

    client = client_service.add_client(aggregated.client.model_dump())
    rule = rule_service.save_rule(aggregated.rule.model_dump())

    rule_service.add_client_to_rule(rule, client)
