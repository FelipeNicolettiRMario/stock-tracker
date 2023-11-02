from .base import Base

from typing import Optional
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.types import VARCHAR, NUMERIC

class Rule(Base):

    __tablename__ = "rule"
     
    id: Mapped[int] = mapped_column(primary_key=True)
    period: Mapped[int] = mapped_column(nullable=False)
    operator: Mapped[bool] = mapped_column(nullable=False)
    target: Mapped[Optional[NUMERIC(5,2)]]
    comparison_target: Mapped[Optional[VARCHAR(7)]]

    UniqueConstraint("period", "operator", "target","comparison_target")
