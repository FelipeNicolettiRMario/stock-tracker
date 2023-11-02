from .base import Base

from sqlalchemy import Column, Table, ForeignKey

RuleToClient = Table(
    "rule_to_client",
    Base.metadata,
    Column("client_id", ForeignKey("client.id")),
    Column("rule_id", ForeignKey("rule.id"))
)
