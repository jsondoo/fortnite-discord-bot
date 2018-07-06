# Fortnite Discord Bot

Simple discord bot that retrieves fortnite user stats

![](https://i.imgur.com/khZNKIG.png)

### Prerequisites

This script requires these libraries: [discord.py](https://github.com/Rapptz/discord.py) and [requests](https://github.com/requests/requests)

```
pip install discord.py
pip install requests
```

### Running the bot

In `bot.py`, replace the values of `BOT_TOKEN` and `FORTNITE_API_TOKEN` with your own API keys.

Discord Developers: [https://discordapp.com/developers/docs/intro](https://discordapp.com/developers/docs/intro)

Fortnite Tracker API: [https://fortnitetracker.com/site-api](https://fortnitetracker.com/site-api)

Run your bot with:

```
python bot.py
```

### Using the bot

Go to a Discord server with your bot, then type `!ping` to check that the bot is online and responding to your messages. The bot must have `VIEW_CHANNEL` and `SEND_MESSAGES` permissions in that Discord server in order to respond to you. 

Type `!stats <platform> <nickname>` to retrieve stats about user with nickname on a platform (pc, xbl, or psn)

The command prefix can be customzied by changing the value of `COMMAND_PREFIX` in `bot.py`.

## Hosting the bot on Heroku

The bot can be hosted for free by running the script on Heroku.

1) Install git and Heroku CLI.

2) Create `requirements.txt` by typing `pip freeze > requirements.txt`. This lets Heroku detect that you are running a Python app and have it install the required libraries.

3) Create a Procfile with `worker: python bot.py`.

4) Create a git repository with `git init`.

5) Create a heroku app and set config vars:

```
heroku login
heroku create
heroku config:set BOT_TOKEN=<insert token here>
heroku config:set FORTNITE_API_TOKEN=<insert token here>
```

6) Push to heroku:

```
git init
git add -A
git commit -m "Initial commit"
git push heroku master
```

6) Start the worker with `heroku ps:scale worker=1`.

7) Check logs with `heroku logs --tail`.


## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
