from abc import ABC, abstractmethod
from typing import Callable

from linebot import LineBotApi


class CommandStrategy(ABC):
    @abstractmethod
    def run(self, line_bot_api: LineBotApi, reply_token: str):
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

    def run(self, line_bot_api: LineBotApi, reply_token: str,) -> None:
        self._command.run(line_bot_api=line_bot_api, reply_token=reply_token)
