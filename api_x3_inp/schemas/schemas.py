from enum import Enum

from pydantic import BaseModel


class SimNao(int, Enum):
    NAO = 1
    SIM = 2


class Message(BaseModel):
    message: str
