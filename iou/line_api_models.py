from pydantic import BaseModel


class Source(BaseModel):
    sender_id: str
    type: str


class SourceGroup(Source):
    user_id: str
    group_id: str


class Message(BaseModel):
    id: str
    type: str
    text: str


class MsgEvent(BaseModel):
    mode: str
    type: str
    timestamp: int
    reply_token: str
    source: SourceGroup
    message: Message


class JoinEvent(BaseModel):
    mode: str
    type: str
    reply_token: str
    timestamp: int
    source: Source
