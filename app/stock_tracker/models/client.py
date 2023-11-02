from .base import Base

from typing import List
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Client(Base):

    __tablename__ = "client"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(unique=True)
    phone: Mapped[str] = mapped_column(unique=True)

    @staticmethod
    def from_dict(data: dict):
        return Client(
            name=data.get("name"),
            email=data.get("email"),
            phone=data.get("phone")
        )
    
    def update_value(self, data: dict):

       self.email = data.get("email") if self.email != data.get("email") and data.get("email") else self.email
       self.phone = data.get("phone") if self.phone != data.get("phone") and data.get("phone") else self.phone
       self.name = data.get("name") if self.phone != data.get("name") and data.get("name") else self.name
