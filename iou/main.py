import logging
import os
import re

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request, Depends
from fastapi.logger import logger
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import JoinEvent, MessageEvent, TextMessage, TextSendMessage


from .db import crud, models
from .db.schemas import GroupCreate
from .db.database import SessionLocal, engine
from .command import command_to_strategy
from .config import COMMAND_PATTERN, USAGE, WELCOME_MESSAGE
from .line_api_models import MsgEvent

load_dotenv()
line_bot_api = LineBotApi(os.getenv("CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.getenv("CHANNEL_SECRET"))
app = FastAPI()
models.Base.metadata.create_all(bind=engine)
logging.basicConfig(level=2, format="%(asctime)-15s %(levelname)-8s %(message)s")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/callback")
async def callback(request: Request):
    # get X-Line-Signature header value
    signature: str = request.headers["X-Line-Signature"]
    # get request body as text
    body: bytes = await request.body()
    decode_body: str = body.decode()
    logger.info("Request body: {}".format(decode_body))
    # handle webhook body
    try:
        handler.handle(decode_body, signature)
    except InvalidSignatureError:
        HTTPException(status_code=400, detail="Invalid Signature")
    return "OK"


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event: MsgEvent):
    msg_text = event.message.text
    match_result = re.match(COMMAND_PATTERN, msg_text)
    if (
        match_result is not None
        and match_result["prefix"]
        and match_result["command"] is None
    ):
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=USAGE))
    elif match_result is not None and match_result["prefix"]:
        subcommand = match_result["command"].strip()
        cmd = command_to_strategy[subcommand]
        cmd.run(line_bot_api, event.reply_token)
    else:
        return "OK"


@handler.add(JoinEvent)
def handle_join_group(event: JoinEvent):
    group_id: str = event.source.sender_id
    logger.info(f"GroupId: {group_id}")
    line_bot_api.reply_message(event.reply_token, TextSendMessage(text=WELCOME_MESSAGE))
    return "OK"
