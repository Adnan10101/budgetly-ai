from src import (
    notion_client,
    llm
)

def setup_bot(bot):
    @bot.event
    async def on_ready():
        print(f'We have logged in as {bot.user}')

    @bot.command()
    async def budget(ctx):
        user_input_text = ctx.message.content[len("$$budget "):] 
        try:
            content = llm.extract_data(user_input_text)
            print("::::::::::",content)
            notion_client.insert_data(content["category_name"], content["name"],content["amount"], content["date"])
            await ctx.send("Successfully added!")
        except Exception as e:
            await ctx.send(f"Error:{e}")
        
      
        


