import discord
import asyncio
import requests
import config

BOT_TOKEN = config.BOT_TOKEN
FORTNITE_API_TOKEN = config.FORTNITE_API_TOKEN

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as '  + client.user.name)

@client.event
async def on_message(message):
  if message.content.startswith('!stats'):
    words = message.content.split(' ')

    if len(words) < 3 or len(words) > 3:
      await client.send_message(message.channel, 'Usage: !stats <pc,xbl,psn> <nickname>')
    elif words[1] not in ('pc','xbl','psn'):
      await client.send_message(message.channel, 'Usage: !stats <pc,xbl,psn> <nickname>')
    else:
      res = fortnite_tracker_api(words[1],words[2])
      if res:
        await client.send_message(message.channel, res)
      else:
        await client.send_message(message.channel, 'Failed to get data')

def fortnite_tracker_api(platform, nickname):
  URL = 'https://api.fortnitetracker.com/v1/profile/' + platform + '/' + nickname
  req = requests.get(URL, headers={"TRN-Api-Key": FORTNITE_API_TOKEN})

  if req.status_code == 200:
    try:
      lifetime_stats = req.json()['lifeTimeStats']
      return lifetime_stats[7:]
    except KeyError:
      return False
  else:
    return False

client.run(BOT_TOKEN)