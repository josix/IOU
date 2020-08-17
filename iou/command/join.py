from typing import Callable

from linebot import LineBotApi
from linebot.models import TextSendMessage

from .command import CommandStrategy


class Join(CommandStrategy):
    def run(
        self, line_bot_api: LineBotApi, reply_token: str,
    ):
        line_bot_api.reply_message(reply_token, TextSendMessage(text="Join"))
