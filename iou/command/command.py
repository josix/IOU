from abc import ABC, abstractmethod
from typing import Optional

from linebot import LineBotApi
from sqlalchemy.orm import Session

from iou.line_api_models import MsgEvent


class CommandStrategy(ABC):
    @abstractmethod
    def run(
        self, event: MsgEvent, line_bot_api: LineBotApi, db: Optional[Session] = None
    ):
        pass


class CommandContext:
    def __init__(self, command: CommandStrategy,) -> None:
        self._command = command

    @property
    def command(self) -> CommandStrategy:
        return self._command

    @command.setter
    def command(self, command: CommandStrategy) -> None:
        self._command = command

    def run(
        self, event: MsgEvent, line_bot_api: LineBotApi, db: Optional[Session] = None
    ) -> None:
        self._command.run(event, line_bot_api, db)
