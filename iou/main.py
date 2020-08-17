import logging
import os
import re

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request
from fastapi.logger import logger
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

from .command import command_to_strategy
from .config import USAGE, COMMAND_PATTERN
from .types import MsgEvent

load_dotenv()
line_bot_api = LineBotApi(os.getenv("CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.getenv("CHANNEL_SECRET"))
app = FastAPI()
logging.basicConfig(level=2, format="%(asctime)-15s %(levelname)-8s %(message)s")


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
