from fastapi import APIRouter
from fastapi.responses import JSONResponse
from http import HTTPStatus

from app.stock_tracker.protocol.rest.models.aggregates import AggregateClientAndRule
from app.stock_tracker.protocol.rest.controllers.save_client_and_rule import save_client_and_rule_controller

router = APIRouter(prefix="/client-and-rule")

@router.post("/add")
def add_client_and_rule(body: AggregateClientAndRule) -> JSONResponse:

    save_client_and_rule_controller(body)

    return JSONResponse(
        {"detail":"Client and rule saved with sucess"},
        status_code=HTTPStatus.CREATED
    )
