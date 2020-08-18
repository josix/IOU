from typing import Optional

from linebot import LineBotApi
from linebot.models import TextSendMessage
from sqlalchemy.orm import Session

from iou.db.crud import create_user
from iou.db.schemas import UserCreate
from iou.line_api_models import MsgEvent

from .command import CommandStrategy


class Join(CommandStrategy):
    def run(
        self, event: MsgEvent, line_bot_api: LineBotApi, db: Optional[Session] = None
    ):
        group_id, user_id = event.source.sender_id, event.source.user_id
        user_profile = line_bot_api.get_group_member_profile(
            group_id=group_id, user_id=user_id
        )
        user = UserCreate(
            display_name=user_profile.display_name, line_id=user_profile.user_id
        )
        # TODO: Check if user duplicated
        # TODO: Relationship with group
        if db is not None:
            db_user = create_user(db, user)
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=f"{db_user.display_name} Joined"),
            )
        else:
            line_bot_api.reply_message(
                event.reply_token, TextSendMessage(text="JoinError")
            )
