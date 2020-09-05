import sys
import random
import discord
from googlesearch import search

client = disocrd.Client()
token = os.environ['DISCORD_BOT_TOKEN']

ModeFlag = 0

@client.event
async def on_message(message):
    global ModeFlag
    if message.author.bot:
        return
    if message.content == "/by"
        await message.channel.send('おｋ')
        sys.exit()
    if ModeFlag == 1:
        kensaku = message.content
        ModeFlag = 0
        count = 0
        for url in search(kensaku, lang="jp",num = 5):
            await message.channel.send(url)
            count += 1
            if(count == 5):
                break
    if mesasge.content == '/google':
        ModeFlag = 1
        await message.channel.send('検索したいワードを発言してください。')
            
    
client.run(token)
