from main_celery import app
from app.stock_tracker.services.factory import ServiceFactory


@app.task
def trigger_rule(rule_id: int):

    rule_service = ServiceFactory.get_rule_service()

    rule = rule_service.get_single_rule(rule_id)
    print(rule)