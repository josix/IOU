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


class Source(BaseModel):
    sender_id: str
    type: str


class JoinEvent(BaseModel):
    mode: str
    type: str
    reply_token: str
    timestamp: int
    source: Source
