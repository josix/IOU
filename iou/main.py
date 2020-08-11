import logging
import os

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException, Request
from fastapi.logger import logger
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

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
    if msg_text == "Add me":
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=msg_text))
