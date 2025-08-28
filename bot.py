import discord
import requests
import random
import os
from discord import app_commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')  # Loaded from .env file

intents = discord.Intents.default()
intents.messages = True
client = discord.Client(intents=intents)
class MyClient(discord.Client):
    def __init__(self, *, intents):
        super().__init__(intents=intents)
        self.tree = app_commands.CommandTree(self)

client = MyClient(intents=intents)
MEME_API_URL = 'https://meme-api.com/gimme/'

async def fetch_meme(subreddit=None):
    url = MEME_API_URL
    if subreddit:
        url += subreddit
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get('url'), data.get('title')
    return None, None

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    try:
        synced = await client.tree.sync()
        print(f'Synced {len(synced)} command(s)')
    except Exception as e:
        print(f'Error syncing commands: {e}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.startswith('!meme'):
        # Extract subreddit/topic if provided
        parts = message.content.split()
        subreddit = parts[1] if len(parts) > 1 else None
        meme_url, title = await fetch_meme(subreddit)
        if meme_url:
            await message.channel.send(f"{title}\n{meme_url}")
        else:
            await message.channel.send("Couldn't fetch a meme right now. Try again later!")
    else:
        # Respond to any message with a random meme based on keywords
        keywords = ['cat', 'dog', 'programming', 'funny', 'dankmemes', 'wholesomememes']
        chosen = random.choice(keywords)
        meme_url, title = await fetch_meme(chosen)
        if meme_url:
            await message.channel.send(f"Here's a meme for you!\n{title}\n{meme_url}")

if __name__ == "__main__":
    if not TOKEN:
        print("Please set the DISCORD_BOT_TOKEN environment variable.")
    else:
        client.run(TOKEN)

# Slash command: /ping
@client.tree.command(name="ping", description="Replies with Pong!")
async def ping_command(interaction: discord.Interaction):
    await interaction.response.send_message("Pong!")
