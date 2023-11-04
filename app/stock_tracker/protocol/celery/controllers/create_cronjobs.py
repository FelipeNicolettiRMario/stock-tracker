from main_celery import app
from celery.schedules import crontab

from app.stock_tracker.services.factory import ServiceFactory
from app.stock_tracker.models.rule import Rule

from .execute_rule import trigger_rule
        
def create_cronjob_from_rule(sender):

    rules_service = ServiceFactory.get_rule_service()

    rules = rules_service.get_all_rules()

    for rule in rules:
        sender.add_periodic_task(
            crontab(rule[0].period),
            trigger_rule.s(rule[0].id)
        )
