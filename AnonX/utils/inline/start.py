from typing import Union
from pyrogram.types import InlineKeyboardButton


def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴩ",
                url=f"https://t.me/{bot.username}?start=help",
            )
        ],
        [
            InlineKeyboardButton(
                text="ᴜᴘᴅᴀᴛᴇs",
                url=f"{SUPPORT_CHANNEL}",
            ),
            InlineKeyboardButton(
                text="sᴜᴘᴘᴏʀᴛ",
                url=f"{SUPPORT_GROUP}",
            )
        ],
        [
            InlineKeyboardButton(
                text="sᴇᴛᴛɪɴɢs", callback_data="settings_helper"
            )
        ]
    ]
    return buttons

def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕",
                url=f"https://t.me/{bot.username}?startgroup=true"),
        ],
        [
            InlineKeyboardButton(
                text="ᴜᴘᴅᴀᴛᴇs",
                url=f"{SUPPORT_CHANNEL}"),
            InlineKeyboardButton(
                text="sᴜᴘᴘᴏʀᴛ",
                url=f"{SUPPORT_GROUP}")
        ],
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴩ",
                callback_data="settings_back_helper"
            )
        ]
    ]
    return buttons

def private_panelx(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="➕ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ➕",
                url=f"https://t.me/{bot.username}?startgroup=true"),
        ],
        [
            InlineKeyboardButton(
                text="ʜᴇʟᴩ",
                callback_data="settings_back_helper"
            )
        ]
    ]
    return buttons
