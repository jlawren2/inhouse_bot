from discord.ext import commands
from discord.ext.commands import ConversionError
from sqlalchemy import Enum
import rapidfuzz

positions_list = ["ONE", "TWO", "THREE", "FOUR", "FIVE"]
position_enum = Enum(*positions_list, name="position_enum")

side_enum = Enum("DEFENDERS", "ATTACKERSS", name="team_enum")

foreignkey_cascade_options = {"onupdate": "CASCADE", "ondelete": "CASCADE"}

# This is a dict used for fuzzy matching





