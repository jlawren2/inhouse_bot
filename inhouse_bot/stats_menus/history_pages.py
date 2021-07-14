from collections import Counter
from typing import Tuple, List

from discord import Embed
from discord.ext import menus


from inhouse_bot.database_orm import GameParticipant, Game

entries_type = List[Tuple[Game, GameParticipant]]


class HistoryPagesSource(menus.ListPageSource):
    def __init__(self, entries: entries_type, bot, player_name, is_dms=False):
        self.bot = bot
        self.player_name = player_name
        self.is_dms = is_dms
        super().__init__(entries, per_page=10)

    async def format_page(self, menu: menus.MenuPages, entries: entries_type):
        embed = Embed()

        embed.set_footer(
            text=f"Page {menu.current_page + 1} of {self._max_pages} "
            f"| Use !champion [name] [game_id] to save champions"
        )

        rows = []

        max_game_id_length = max(len(str(game.id)) for game, participant in entries)

        for game, participant in entries:
            champion_emoji = get_champion_emoji(participant.champion_id, self.bot)


            if not game.winner:
                result = "⚔"
            elif game.winner == participant.side:
                result = "✅"
            else:
                result = "❌"

            id_padding = max_game_id_length - len(str(game.id)) + 2

            # TODO LOW PRIO add pre-game MMR
            output_string = (
                f"{result}     {champion_emoji}  "
                f"`#{game.id}{' '*id_padding}{game.start.date()}"
                + ("`" if not self.is_dms else f"  {self.bot.get_guild(game.server_id).name}`")
            )

            rows.append(output_string)


        embed.add_field(name=f"{self.player_name}’s match history", value="\n".join(rows))

        return embed
