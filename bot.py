from keep_alive import keep_alive
import discord
import random
import asyncio
from googlesearch import search

TOKEN = ''


client = discord.Client()


responses = ["You Will Live To 100", "You Will Run In To A Wall Today", "You Will Be Over 6 Feet Tall", "You Will Be Rich", "You Will Eat Pizza Today", "You Will Win A Million Dollars"]


coin = ["heads", "tails"]





@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("ping"):
        await message.channel.send('pong')

    if message.content.startswith("say"):
        mes = message.content.split()
        output = ""
        for word in mes [1]:
            output += word
            output += " "
        await message.channel.send(output)
        await message.delete()

    if message.content.startswith("magic8ball"):
        await  message.channel.send(random.choice(responses))
    if message.content.startswith("coinflip"):
        await message.channel.send(random.choice(coin))

    if message.content.startswith("help"):
        embed = discord.Embed(title="__Command__", color=0x00ff00)
        embed.add_field(name='help', value='Shows this message')
        await message.channel.send(content=None, embed=embed)

    if message.content.startswith("hello"):
        channel = message.channel
        await channel.send("Hey \n"
                           "do you want to play heads or tails?")



        def check(m):
            return m.content in ("yes", "Yes", "Sure", "sure")

        msg = await client.wait_for("message", check=check)
        await channel.send("Ok \n"""
                           "I pick \n")
        await  channel.send(random.choice(coin))
        await channel.send("The Winner is.....")
        await channel.send(random.choice(coin))
        
     if message.content.startswith("random number")
        await channel.send(random.randint(1, 200))


@client.event
async def on_message2(message):
    if message.content.startswith('google'):
        searchContent = ""
        text = str(message.content).split(' ')
        for i in range(2, len(text)):
            searchContent = searchContent + text[i]

        for j in search(searchContent, tld="co.in", num=1, stop=1, pause=2):
            await message.channel.send(j)


@client.event
async  def on_ready():
    print("ammazing")




client.run(TOKEN)
print(client.user.name)
