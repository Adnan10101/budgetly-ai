import src.notion_client as notion_client

def setup_bot(bot):
    @bot.event
    async def on_ready():
        print(f'We have logged in as {bot.user}')

    @bot.command()
    async def budget(ctx):
        a = notion_client.results()
        #print(a.keys())
        print(a)
        await ctx.send("lol")
       