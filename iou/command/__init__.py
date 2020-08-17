from collections import defaultdict
from typing import Dict

from .command import CommandContext
from .join import Join
from .wrong_command import WrongCmd

command_to_strategy: Dict[str, CommandContext] = defaultdict(
    lambda: CommandContext(WrongCmd())
)
command_to_strategy.update({"join": CommandContext(Join())})
__all__ = "command_to_strategy"
