from pydantic import BaseModel, root_validator
from typing import Optional

class Rule(BaseModel):

    ticker: str
    period: int
    operator: bool
    target: Optional[float] = None
    comparison_target: Optional[str] = None

    @root_validator
    def validate_if_models_has_target_or_comparison_target(cls):

        if not cls.target and not cls.comparison_target:
            raise ValueError("Input need a target or a comparison_target")
        
        return cls