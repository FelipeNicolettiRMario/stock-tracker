from .base import Base
from .rule_to_client import RuleToClient
from .client import Client

from typing import Optional, List
from sqlalchemy import UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import VARCHAR, NUMERIC

class Rule(Base):

    __tablename__ = "rule"
     
    id: Mapped[int] = mapped_column(primary_key=True)
    ticker: Mapped[str] = mapped_column(nullable=False)
    period: Mapped[int] = mapped_column(nullable=False)
    operator: Mapped[bool] = mapped_column(nullable=False)
    target: Mapped[Optional[float]]
    comparison_target: Mapped[Optional[str]]

    clients: Mapped[List[Client]] = relationship(secondary=RuleToClient)

    UniqueConstraint("period", "operator", "target","comparison_target", "ticker")

    @staticmethod
    def from_dict(data: dict):
        return Rule(
            period=data.get("period"),
            operator=data.get("operator"),
            target=data.get("target"),
            comparison_target=data.get("comparison_target"),
            ticker=data.get("ticker")
        )
