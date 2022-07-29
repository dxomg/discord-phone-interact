import os
import sys
import discord
import psutil
from discord.ext import commands

MOTD = "Bot Has Started!"

client = commands.Bot(command_prefix=',')
client.remove_command('help')

@client.event
async def on_ready():
    print(f"{MOTD}")

@client.command()
async def msg(ctx, *, arg: str):
    os.system(f"termux-notification -t '{arg}'")
    embed = discord.Embed(title="Message Sent", description=f";)", color=discord.Color.blue())
    await ctx.send(embed=embed)
    
@client.command() 
async def tts(ctx, *, arg: str):
    os.system (f"termux-tts-speak -p 1 '{arg}'")
    embed = discord.Embed(title="Voice Message Sent", description=f";)", color=discord.Color.blue())
    await ctx.send(embed=embed)
    
@client.command()
async def popup(ctx, *, arg: str):
    os.system (f"termux-toast -b green -g top '{arg}'")
    embed = discord.Embed(title="Popup Sent", description=f";)", color=discord.Color.blue())
    await ctx.send(embed=embed)
    
client.run("YOUR TOKEN")
