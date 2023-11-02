from pydantic import BaseModel, model_validator
from typing import Optional

class Rule(BaseModel):

    ticker: str
    period: int
    operator: bool
    target: Optional[float] = None
    comparison_target: Optional[str] = None

    @model_validator(mode="before")
    def validate_if_models_has_target_or_comparison_target(cls, field_values):

        if not field_values["target"] and not field_values["comparison_target"]:
            raise ValueError("Input need a target or a comparison_target")
        
        return field_values