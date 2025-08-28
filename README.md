# Discord Meme Generator Bot
This bot was deployed at 4:00 a.m., when normal people sleep and developers question their life choices. It doesn’t have a /therapy command yet, but considering the deployment stress, maybe it should. If it crashes, don’t blame the bot. Blame the AWS free tier. Star this repo if you smiled at least once while reading this — or if you didn’t, because guilt-tripping works too. A Discord bot that responds to user messages and slash commands with random memes based on user input. Built with Python, discord.py, and deployed on AWS EC2.

A Discord bot that lives to flood your server with memes — random, topic-based, and occasionally unfunny (but that’s on you, not the bot).
Built with Python, powered by discord.py, and running on AWS EC2 — because free hosting ghosted us at 3 a.m.
## Features
- Responds to `!meme` or `!meme <topic>` with a relevant meme
- Responds to any message with a random meme
- `/ping` slash command replies with `Pong!`
- Easy deployment on AWS EC2 (or any server)

## Setup

### 1. Clone or Download the Project
```
git clone <your-repo-url>
cd "discord bot"
```

### 2. Create a Discord Bot and Get Token
- Go to the [Discord Developer Portal](https://discord.com/developers/applications)
- Create a new application and add a bot
- Copy the bot token
- Invite the bot to your server with the right permissions (Send Messages, Read Messages, Use Slash Commands)

### 3. Configure Environment Variables
Create a `.env` file in the project directory:
```
TOKEN=your_discord_bot_token_here
```

### 4. Install Requirements
#### On Ubuntu (recommended for AWS EC2):
```
sudo apt update
sudo apt install python3 python3-pip python3.12-venv git -y
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
pip install python-dotenv
```

### 5. Run the Bot
```
python bot.py
```

## Usage
- Type `!meme` or `!meme <topic>` in any channel the bot can read
- Use the `/ping` slash command

## Deploying on AWS EC2
1. Launch an Ubuntu EC2 instance
2. SSH into your instance
3. Upload your bot files (use `scp` or `git clone`)
4. Follow the setup steps above
5. (Optional) Use `screen` or `tmux` to keep the bot running after logout

## Keep the Bot Running
To keep your bot running after you disconnect:
```
sudo apt install screen -y
screen -S discordbot
python bot.py
# Press Ctrl+A then D to detach
```

## License
MIT
