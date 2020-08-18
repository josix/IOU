from typing import Optional

from linebot import LineBotApi
from linebot.models import TextSendMessage
from sqlalchemy.orm import Session

from iou.config import WRONG_USAGE_RESPONSE
from iou.line_api_models import MsgEvent

from .command import CommandStrategy


class WrongCmd(CommandStrategy):
    def run(
        self, event: MsgEvent, line_bot_api: LineBotApi, db: Optional[Session] = None
    ):
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(text=WRONG_USAGE_RESPONSE)
        )
