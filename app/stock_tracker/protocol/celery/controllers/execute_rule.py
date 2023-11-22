from main_celery import app
from app.stock_tracker.services.factory import ServiceFactory


@app.task
def trigger_rule(rule_id: int):

    rule_service = ServiceFactory.get_rule_service()
    communication_servcice = ServiceFactory.get_communication_service()

    rule = rule_service.get_single_rule(rule_id)
    
    if rule_service.is_rule_satisfied(rule):
        message_content = f"""Your rule for the stock {rule.ticker} was triggered, actual price is 
        {'greater' if rule.operator else 'lower'} than {rule.target}
        """

        adresses = []
        for client in rule.clients:
            adresses.append(client.email)

        adresses = ",".join(adresses)     

        communication_servcice.send_email(
            message_content,
            "Rule Satisfied!",
            adresses
        )
