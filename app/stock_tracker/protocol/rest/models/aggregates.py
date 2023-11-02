from .client import Client
from .rule import Rule

from pydantic import BaseModel

class AggregateClientAndRule(BaseModel):

    client: Client
    rule: Rule
