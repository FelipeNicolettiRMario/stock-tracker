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

    @staticmethod
    def from_dict(data: dict):
        return Client(
            name=data.get("name"),
            email=data.get("email"),
            phone=data.get("phone")
        )
    
    def update(self, data: dict):

       self.email = data.get("email") if self.email != data.get("email") and data.get("email") else self.email
       self.phone = data.get("phone") if self.phone != data.get("phone") and data.get("phone") else self.phone
       self.name = data.get("name") if self.phone != data.get("name") and data.get("name") else self.name
