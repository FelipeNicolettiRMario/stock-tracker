from fastapi import FastAPI

app = FastAPI()

from app.stock_tracker.protocol.rest.views import save_client_and_rule

app.include_router(save_client_and_rule.router)
