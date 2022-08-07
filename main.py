import os
import discord

from dotenv import load_dotenv

# Loads the .env file
load_dotenv()

# Get the API token from the .env file
tk = os.getenv("TOKEN")

# Create a client object from the discord.py module
bot = discord.Client()

# Listen for when the bot switches states
@bot.event
async def on_ready():
    server_count = 0

    for server in bot.guilds:
        print(f"- {server.id} (name: {server.name})")

        server_count += 1

    print("Derek-Bot is in " + str(server_count) + " guilds.")

# Listen for when a new message is sent
@bot.event
async def on_message(msg):
    # If the message is a command
    if msg.content == "$test":
        await msg.channel.send("confirmed")
        
# Run the bot
bot.run(tk) 
