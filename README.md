# Fortnite Discord Bot

Simple discord bot that retrieves fortnite user stats

### Prerequisites

This script requires these libraries: [discord.py](https://github.com/Rapptz/discord.py) and [requests](https://github.com/requests/requests)

```
pip install discord.py
pip install requests
```

### Running the bot

In `bot.py`, replace the values of `BOT_TOKEN` and `FORTNITE_API_TOKEN` with your own API keys.

Discord Developers: [https://discordapp.com/developers/docs/intro]()

Fortnite Tracker API: [https://fortnitetracker.com/site-api]()

Run your bot with:

```
python bot.py
```

### Using the bot

Go to a Discord server with your bot, then type `!ping` to check that the bot is online and responding to your messages. The bot must have `VIEW_CHANNEL` and `SEND_MESSAGES` permissions in that Discord server in order to respond to you. 

Type `!stats <platform> <nickname>` to retrieve stats about user with nickname on a platform (pc, xbl, or psn)

The command prefix can be customzied by changing the value of `COMMAND_PREFIX` in `bot.py`.

## Hosting the bot externally

Add additional notes about how to deploy this on a live system

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details