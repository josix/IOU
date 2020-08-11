from typing import Optional

from pydantic import BaseModel


class Message(BaseModel):
    id: str
    type: Optional[str] = None
    text: Optional[str] = None


class MsgEvent(BaseModel):
    mode: str
    type: str
    timestamp: int
    reply_token: str
    message: Message
