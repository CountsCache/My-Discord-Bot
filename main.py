import discord
import requests
import json
from keep_alive import keep_alive
import music

import os

cogs = [music]

client = discord.Client()

for i in range(len(cogs)):
  cogs[i].setup(client)

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

  if message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if message.content.startswith('$wink'):
    waifu = get_waifu()
    await message.channel.send(waifu)

# this keeps the webserver running
keep_alive()
#add music player cog
bot.add_cog(Player(bot))
#Use TOKEN variable to run bot (keep secret)
TOKEN = os.environ['key']
client.run(TOKEN)
bot.run(TOKEN)