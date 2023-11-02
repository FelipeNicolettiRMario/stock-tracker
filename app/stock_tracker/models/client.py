from .base import Base
from .rule_to_client import RuleToClient
from .rule import Rule

from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.types import VARCHAR

class Client(Base):

    __tablename__ = "client"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[VARCHAR(50)] = mapped_column(nullable=False)
    email: Mapped[VARCHAR(70)] = mapped_column(unique=True)
    phone: Mapped[VARCHAR(20)] = mapped_column(unique=True)

    rules: Mapped[List[Rule]] = relationship(secondary=RuleToClient, back_populates="clients")