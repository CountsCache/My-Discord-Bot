import discord
import requests
import json

import os

client = discord.Client()

for i in range(len(cogs)):
  cogs[i].setup(client)

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)


# gets a random winking gif from the waifu api when a user uses the command $wink
def get_waifu():
  response = requests.get("https://api.waifu.pics/sfw/wink")
  json_data = json.loads(response.text)
  waifu = "*LOADING WINK...* \n " + json_data['url']
  return(waifu)

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
  if message.author == client.user:
    return

    if message.content.startswith('$wink'):
    waifu = get_waifu()
    await message.channel.send(waifu)

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

  if message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

#Use TOKEN variable to run bot (keep secret)
TOKEN = os.environ['key']
client.run(TOKEN)
bot.run(TOKEN)
