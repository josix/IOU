from pydantic import BaseModel


class Message(BaseModel):
    id: str
    type: str
    text: str


class MsgEvent(BaseModel):
    mode: str
    type: str
    timestamp: int
    reply_token: str
    message: Message
