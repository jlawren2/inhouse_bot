import os
import re
from typing import Optional, Union

import lol_id_tools
from discord import Emoji
import inflect

# Used to properly name numerals
inflect_engine = inflect.engine()

# Raw images for embed thumbnails
cdragon_root = "https://raw.communitydragon.org/latest/plugins/rcp-fe-lol-clash/global/default/assets/images"
positions_pictures_url = cdragon_root + "/position-selector/positions/icon-position-"

lol_logo = (
    "https://raw.communitydragon.org/10.5/plugins/rcp-fe-lol-loading-screen/global/default/lol_icon.png"
)

# Emoji dict built from environment variables


# Default rank emoji
rank_emoji_dict = {
    1: "π₯",
    2: "π₯",
    3: "π₯",
    10: "\N{KEYCAP TEN}",
    **{i: str(i) + "\u20e3" for i in range(4, 10)},
}

def get_rank_emoji(rank: int) -> str:
    if rank > 9:
        rank_str = inflect_engine.ordinal(rank + 1)
        return f"`{rank_str}`β―"
    else:
        return rank_emoji_dict[rank + 1] + "β―β―"


no_symbols_regex = re.compile(r"[^\w]")


def get_champion_emoji(emoji_input: Optional[Union[int, str]], bot) -> str:
    """
    Accepts champion IDs, "loading", and None
    """
    emoji_name = None
    fallback = None

    if emoji_input is None:
        return "β"
    elif emoji_input == "loading":
        emoji_name = emoji_input
        fallback = "β"
    elif type(emoji_input) == int:
        fallback = lol_id_tools.get_name(emoji_input, object_type="champion")
        emoji_name = no_symbols_regex.sub("", fallback).replace(" ", "")

    for emoji in bot.emojis:
        emoji: Emoji
        if emoji.name == emoji_name:
            return str(emoji)

    # Fallback that should only be reached when we donβt find the rights emoji
    return fallback
