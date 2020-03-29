# Mark rewrite. Wonder how this'll go.
import discord, random, time, aiohttp, os, json, asyncio
from discord.ext import commands

client = commands.Bot(command_prefix = '!')
client.remove_command('help')

# Status, also, for when I get back to cycled statuses: ['Mario Royale', 'DMCA Royale', 'Half Life 3', 'Animal Crossing: New Horizons', 'DOOM Eternal', 'Super Mario World']
@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game('Animal Crossing: New Horizons'))
    print("Mark is running!")
    
# Help. The reason why this isn't in the other commands is because it isn't really fit for them.
@client.command(pass_context=True)
async def help(ctx):
    embed = discord.Embed(
        colour = discord.Colour.orange()
    )
    
    embed.set_author(name="Help")
    embed.add_field(name=".ping", value="Returns the client latency.", inline=False)
    embed.add_field(name=".crush", value="Tells you your crush, as simple as that.", inline=False)
    embed.add_field(name=".coin", value="Flip a coin. .coinflip also works.", inline=False)
    
    await ctx.send(embed=embed)

# Fun Commands
@client.command()
async def ping(ctx):
    await ctx.send(f"Pong! `{round(client.latency * 1000)}`ms")

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    responses = ["Certainly.", "It is decidedly so.", "Doubtless.", "Yes - definitely.", "You can rely on it.", "Yes.", "No.", "My reply is no.", "Don't count on it.", "The sign says no.", "Doubtful."]
    await ctx.send(f"{random.choice(responses)}")

@client.command(aliases=['coinflip'])
async def coin(ctx):
    flip = ["Heads!", "Tails!"]
    await ctx.send("Flipping...")
    time.sleep(1)
    await ctx.send(f"{random.choice(flip)}")

@client.command()
async def ship(ctx):
    ships = ["Micah X Megumin", "LinkyTay X Natalie", "Natalie X Sarah", "Terminal X Megumin", "TalionDiscord X Chrisoman", "LinkyTay X YellowDude", "Micah X YellowDude", "Micah X Minus", "YellowDude X Megumin", "Mario X Luigi", "Mario X Peach", "ddmilburn02 X Eliza", "ddmilburn02 X Cyuubi", "Eliza X Cyuubi"]
    await ctx.send(f"{random.choice(ships)}")

@client.command()
async def crush(ctx):
    crushList = ["Cyuubi", "Natalie", "Sarah", "LinkyTay", "Micah", "Captain", "Somari the Adventurer", "Eliza", "DDMil", "JaeDoh", "Kev", "Neil", "Home Invader Tax Evader", "Arcade Gamer", "LeoX", "GRAnimated", "Paulo", "Nuts & Milk", "Pixelcraftian", "InfernoPlus", "OneSome", "Megumin", "BakerDaGamer464", "Simonixen07", "minus", "Mariocoder", "ATVdriver", "YellowDude", "Darksselia", "PK Rockin", "*insert joke* Guy", "Wolfgalaxy", "me", "Thesless", "Markette", "NethoWarrior"]
    await ctx.send(f"Your crush is {random.choice(crushList)}")

# To run the bot. The os.environ locates the config var in the Heroku app, this is done to secure the token. Nice try, Eliza! 
client.run(os.environ['TOKEN'])
