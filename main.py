import discord
from discord.ext import commands
# import src.discord_bot as discord_bot
# import src.notion_client as notion_client
# import src.llm as llm
from src import (
   notion_client,
   discord_bot,
   llm,
)

from src.utils.config import DISCORD_TOKEN, NOTION_API


intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix = "$$", intents = intents)

if __name__ == "__main__":
   # discord_bot.setup_bot(bot)
   # bot.run(DISCORD_TOKEN)
   #notion_client.insert_data("Groceries","bull",100,"2025-02-24")
   #llm.call_llm("")
   llm.extract_data("hello, i made a purchase of 50$ of groceries from foodbasics on 15 jan")
