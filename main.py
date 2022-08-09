import discord
import sqlite3

from discord.ext import commands

intents = discord.Intents.default()
intents.members = True

# Create a client object from the discord.py module
bot = commands.Bot(command_prefix='$', intents=intents)

# Listen for when someone joins the server
# Create database table if it doesn't exist
# Adds new users to the database
@bot.event
async def on_member_join(user):    
    # Establish connection to database
    connection = sqlite3.connect('users.db')
    cursor = connection.cursor()

    # Create the table if it doesn't already exist
    create_query = """CREATE TABLE IF NOT EXISTS users (id INTEGER, xp INTEGER)"""
    cursor.execute(create_query)

    # Select only the user ID column
    select_query = """SELECT id FROM users"""
    cursor.execute(select_query)
    
    ids = {data[0] for data in cursor.fetchall()}
    
    if not user.id in ids:
        cursor.execute("""INSERT INTO users (id, xp) VALUES (?, ?)""", (user.id, 0))
        print(f"Added {user.id} to the database.")
    else:
        print(f"{user.id} is already in the database.")
    
    # Commit changes and close connection
    connection.commit()
    cursor.close()
    connection.close()
    
    # Get the welcome channel ID
    channel = bot.get_channel(1006419916351611051)
    
    # Send new member welcome message
    # await channel.send(f"{user.mention} has joined the server!")
    print("User joined")

# Listen for when the bot switches states
@bot.event
async def on_ready():
    server_count = 0

    for server in bot.guilds:
        # print(f"- {server.id} (name: {server.name})")
        server_count += 1

    print("Derek-Bot is online in " + str(server_count) + " servers.")

# Listen for when a new message is sent
@bot.event
async def on_message(msg):
    # If the message is a command
    if msg.content == "test":
        await msg.channel.send("confirmed")
        
# Run the bot
bot.run("MTAwNTcxMjQ5MzEwMTk4NTgwMg.GeF0Ad.UIy5V6YRalYqmU1z7K5vw631sELTL7K9dyZKU4") 
