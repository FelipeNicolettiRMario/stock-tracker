from dotenv import load_dotenv
from celery import Celery
import os

load_dotenv()
redis_url = os.getenv("REDIS_URL", "redis://localhost:6379")

app = Celery("stock.tracker", include=["app.stock_tracker.protocol.celery.controllers.create_cronjobs"])
app.conf.broker_url = redis_url
app.conf.result_backend = redis_url
app.conf.event_serializer = "json"
app.conf.task_serializer = "json"
app.conf.result_serializer = "json"

@app.on_after_configure.connect
def transform_all_rules_in_cronjobs(sender, **k):
    from app.stock_tracker.protocol.celery.controllers.create_cronjobs import create_cronjob_from_rule

    create_cronjob_from_rule(sender)
    

