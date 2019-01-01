import discord
from discord.ext.commands import Bot
from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType
import asyncio
import platform
import colorsys
import random
import os
import time
from discord.voice_client import VoiceClient
from discord import Game, Embed, Color, Status, ChannelType
import traceback
import string
import inspect
import json
from cleverwrap import CleverWrap
import config
import utils
import aiohttp
import websockets
from bs4 import BeautifulSoup
import urllib.request
import logging
import colorsys
import socket
import praw
import datetime

Forbidden= discord.Embed(title="Permission Denied", description="1) Please check whether you have permission to perform this action or not. \n2) Please check whether my role has permission to perform this action in this channel or not. \n3) Please check my role position.", color=0x00ff00)

bot = commands.Bot(description="Republic Of allipsters", command_prefix=commands.when_mentioned_or("A!"), pm_help = True)
bot.remove_command('help')


async def status_task():
    while True:
        await client.cange_presence(game=discord.Game(name='for A!help'))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name='with '+str(len(set(client.get_all_members())))+' users'))
        await asyncio.sleep(5)
        await client.change_presence(game=discord.Game(name='in '+str(len(client.servers))+' servers'))
        await asyncio.sleep(5)

left = '⏪'
right = '⏩'

@bot.event
async def on_ready():
        '''console output on initialization'''
        print('Logged in as')
        print(bot.user.name)
        print(bot.user.id)
        print('------')

@bot.command(pass_context=True)
async def multiply(ctx):
        """multiplies two numbers together"""
        left = float(ctx.message.content.split()[1])
        right = float(ctx.message.content.split()[2])
        header = str(left) + ' * ' + str(right)
        text = str(left * right)

        embed = discord.Embed()
        embed.add_field(name=header, value=text, inline=True)
        await bot.delete_message(ctx.message)
        await bot.say(embed=embed)

@bot.command(pass_context=True)
async def add(ctx):
        """Adds two numbers together."""
        left = float(ctx.message.content.split()[1])
        right = float(ctx.message.content.split()[2])
        header = str(left) + ' + ' + str(right)
        text = str(left + right)

        embed = discord.Embed()
        embed.add_field(name=header, value=text, inline=True)
        await bot.delete_message(ctx.message)
        await bot.say(embed=embed)

@bot.command(pass_context=True)
async def substract(ctx):
        """Subtract two numbers."""
        left = float(ctx.message.content.split()[1])
        right = float(ctx.message.content.split()[2])
        header = str(left) + ' - ' + str(right)
        text = str(left - right)

        embed = discord.Embed()
        embed.add_field(name=header, value=text, inline=True)
        await bot.delete_message(ctx.message)
        await bot.say(embed=embed)

@bot.command(pass_context=True)
async def exponent(ctx):
        """raises the 1st no. to the exponent of the 2nd no."""
        number = float(ctx.message.content.split()[1])
        power = float(ctx.message.content.split()[2])
        header = str(number) + ' to the power of ' + str(power)
        text = str(number ** power)

        embed = discord.Embed()
        embed.add_field(name=header, value=text, inline=True)
        await bot.delete_message(ctx.message)
        await bot.say(embed=embed)

@bot.command(pass_context=True)
async def divide(ctx):
        """divides first number by second number"""
        left = float(ctx.message.content.split()[1])
        right = float(ctx.message.content.split()[2])
        header = str(left) + ' / ' + str(right)
        text = str(left / right)

        embed = discord.Embed()
        embed.add_field(name=header, value=text, inline=True)
        await bot.delete_message(ctx.message)
        await bot.say(embed=embed)

@bot.command()
async def choose(*choices: str):
        """randomly chooses between multiple options"""
        header = 'Bot has randomly chosen...'
        text = random.choice(choices)

        embed = discord.Embed()
        embed.add_field(name=header, value=text, inline=True)
        await bot.say(embed=embed)

@bot.command()
async def magicball():
        '''Answer a question with a response'''

        responses = [
            'It is certain',
            'It is decidedly so',
            'Without a doubt',
            'Yes definitely',
            'You may rely on it',
            'As I see it, yes',
            'Most likely',
            'Outlook good',
            'Yes',
            'Signs point to yes',
            'Reply hazy try again',
            'Ask again later',
            'Better not tell you now',
            'Cannot predict now',
            'Concentrate and ask again',
            'Do not count on it',
            'My reply is no',
            'My sources say no',
            'Outlook not so good',
            'Very doubtful'
        ]

        random_number = random.randint(0, 19)
        if random_number >= 0 and random_number <= 9:
            embed = discord.Embed(color=0x60E87B)
        elif random_number >= 10 and random_number <= 14:
            embed = discord.Embed(color=0xECE357)
        else:
            embed = discord.Embed(color=0xD55050)

        header = 'Magic ball says...'
        text = responses[random_number]

        embed.add_field(name=header, value=text, inline=True)
        await bot.say(embed=embed)

@bot.command()
async def coinflip():
        '''Flips a coin'''

        random_number = random.randint(1, 1000)
        if random_number >= 500:
            text = 'It comes up tails'
        else:
            text = 'It comes up heads'

        header = 'Bot has flipped a coin...'

        embed = discord.Embed()
        embed.add_field(name=header, value=text, inline=True)
        await bot.say(embed=embed)

@bot.command(pass_context=True)
async def rps(ctx):
        ''' Play a game of rps '''
        choice = ctx.message.content.split()[1].lower()
        options = {'rock': 1, 'paper': 2, 'scissors': 3}

        choice = options.get(choice, 0)
        bot_choice = random.randint(1, 3)

        if choice == 0:
            header = 'Error!'
            text = 'Invalid choice! Try again.'
        # 1 > 3 > 2 > 1
        elif choice == 1:
            if bot_choice == 1:
                header = 'Tie!'
                text = 'Bot has chosen rock'
            elif bot_choice == 2:
                header = 'You lose!'
                text = 'Bot has chosen paper'
            elif bot_choice == 3:
                header = 'You win!'
                text = 'Bot has chosen scissors'
        elif choice == 2:
            if bot_choice == 1:
                header = 'You win!'
                text = 'Bot has chosen rock'
            elif bot_choice == 2:
                header = 'Tie!'
                text = 'Bot has chosen paper'
            elif bot_choice == 3:
                header = 'You lose!'
                text = 'Bot has chosen scissors'
        elif choice == 3:
            if bot_choice == 1:
                header = 'You lose!'
                text = 'Bot has chosen rock'
            elif bot_choice == 2:
                header = 'You win!'
                text = 'Bot has chosen paper'
            elif bot_choice == 3:
                header = 'Tie!'
                text = 'Bot has chosen scissors'

        embed = discord.Embed()
        embed.add_field(name=header, value=text, inline=True)
        await bot.say(embed=embed)

@bot.command()
async def repeat(*textstring: str):
        '''get the bot to repeat some input'''
        text = ' '.join(textstring)
        embed = discord.Embed()
        embed.add_field(name='Repeat', value=text, inline=True)
        await bot.say(embed=embed)

@bot.command()
async def addquote(*textstring: str):
        '''Adds quote to list of quotes.'''
        quotes = {}
        with open('quotes.json', 'r') as readfile:
            quotes = json.load(readfile)
            quote_list = quotes['quote_list']

        quotes['quote_list'].append(textstring)

        with open('quotes.json', 'w') as outfile:
            json.dump(quotes, outfile)

        text = "Quote added to database."
        embed = discord.Embed()
        embed.add_field(name='Add Quote', value=text, inline=True)
        await bot.say(embed=embed)

@bot.command()
async def getquote():
        ''' Gets quote from database. '''
        text = ''
        with open('quotes.json', 'r') as readfile:
            quotes = json.load(readfile)
            quote_list = quotes['quote_list']
            text = quote_list[random.randint(0, len(quote_list)-1)]

        text = ' '.join(text)
        embed = discord.Embed()
        embed.add_field(name='Get Quote', value=text, inline=True)
        await bot.say(embed=embed)

@bot.command(pass_context=True)
async def tweet(ctx, usernamename:str, *, txt:str):
    url = f"https://nekobot.xyz/api/imagegen?type=tweet&username={usernamename}&text={txt}"
    async with aiohttp.ClientSession() as cs:
        async with cs.get(url) as r:
            res = await r.json()
            r, g, b = tuple(int(x * 255) for x in colorsys.hsv_to_rgb(random.random(), 1, 1))
            embed = discord.Embed(color = discord.Color((r << 16) + (g << 8) + b))
            embed.set_image(url=res['message'])
            embed.title = "{} twitted: {}".format(usernamename, txt)
            await bot.say(embed=embed)

	
@bot.command(pass_context=True)
async def virus(ctx,user: discord.Member=None,*,hack=None):
    nome = ctx.message.author
    if not hack:
        hack = 'discord'
    else:
        hack = hack.replace(' ','_')
    channel = ctx.message.channel
    x = await bot.send_message(channel, '``[▓▓▓                    ] / {}-virus.exe Packing files.``'.format(hack))
    await asyncio.sleep(1.5)
    x = await bot.edit_message(x,'``[▓▓▓▓▓▓▓                ] - {}-virus.exe Packing files..``'.format(hack))
    await asyncio.sleep(0.3)
    x = await bot.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓           ] \ {}-virus.exe Packing files...``'.format(hack))
    await asyncio.sleep(1.2)
    x = await bot.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓         ] | {}-virus.exe Initializing code.``'.format(hack))
    await asyncio.sleep(1)
    x = await bot.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ] / {}-virus.exe Initializing code..``'.format(hack))
    await asyncio.sleep(1.5)
    x = await bot.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ] - {}-virus.exe Finishing.``'.format(hack))
    await asyncio.sleep(1)
    x = await bot.edit_message(x,'``[▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ] \ {}-virus.exe Finishing..``'.format(hack))
    await asyncio.sleep(1)
    x = await bot.edit_message(x,'``Successfully downloaded {}-virus.exe``'.format(hack))
    await asyncio.sleep(2)
    x = await bot.edit_message(x,'``Injecting virus.   |``')
    await asyncio.sleep(0.5)
    x = await bot.edit_message(x,'``Injecting virus..  /``')
    await asyncio.sleep(0.5)
    x = await bot.edit_message(x,'``Injecting virus... -``')
    await asyncio.sleep(0.5)
    x = await bot.edit_message(x,'``Injecting virus....\``')
    await bot.delete_message(x)
    await bot.delete_message(ctx.message)
        
    if user:
        await bot.say('`{}-virus.exe` successfully injected into **{}**\'s system.'.format(hack,user.name))
        await bot.send_message(user,'**Alert!**\n``You may have been hacked. {}-virus.exe has been found in your system\'s operating system.\nYour data may have been compromised. Please re-install your OS immediately.``'.format(hack))
    else:
        await bot.say('**{}** has hacked himself ¯\_(ツ)_/¯.'.format(name.name))
        await bot.send_message(name,'**Alert!**\n``You may have been hacked. {}-virus.exe has been found in your system\'s operating system.\nYour data may have been compromised. Please re-install your OS immediately.``'.format(hack))
		
@bot.command(pass_context = True)
async def ping(ctx):
    if ctx.message.author.bot:
      return
    else:
      channel = ctx.message.channel
      t1 = time.perf_counter()
      await client.send_typing(channel)
      t2 = time.perf_counter()
      await bot.say("Ping: {}ms".format(round((t2-t1)*1000)))



@bot.command(pass_context=True)
async def help(ctx):
     await bot.say("General Commands | ""\n" "**__rps__** \nBot plays rps with you use it like A!rps \n\n**__magicball__**\nAsk bot anything use it like A!magicball \n\n**__addquote__**\nAdds quote to list of quotes.Use it like A!addquote \n\n**__getquote__**\nGets quote from database.Use it like A!getquote \n\n**__repeat__**\nget the bot to repeat some input.Use it like A!repeat \n\n**__coinflip__**\nflips a coin.Use it likeA!coinflip \n\n**__choose__**\nBot choose between multiple choices.Use it like A!choose \n\n**__divide__**\ndivides a number.Use it like A!divide \n\n**__exponent__**\nraises the 1st no to the exponent of the 2nd no.Use it like A!exponent \n\n**__substract__**\nSubtract two numbers.Use it like A!substract \n\n**__add__**\nAdds two numbers together.Use it like A!add \n\n**__multiply__**\nMultiplies two numbers together.Use it Like A!multiply \n\n**__virus__**\nUse it to virus a user.Use it like A!virus<user> \n\n**__tweet__**Use it to tweet something,like A!tweet<name><tweet>")

bot.run(os.getenv("Token"))
