import discord
import asyncio
import time
import colorsys
from auth import bot_token
client = discord.Client()
initialised = False

def rgb_to_colour(rgb):
    rgb = list(map(lambda x: int(x*255), rgb))
    return discord.Colour((256**2)*rgb[0] + 256*rgb[1] + rgb[2])

@client.event
async def on_ready():
    global initialised
    if not initialised:
        initialised = True
        flash_server = None
        flash_role = None

        for server in client.servers:
            if server.id == "369144280863997962":
                flash_server = server
                break

        for role in flash_server.roles:
            if role.id == "377268081728159744":
                flash_role = role
                break

        colour_count = 20
        colours = [rgb_to_colour(colorsys.hsv_to_rgb(i/colour_count, 1, 1)) for i in range(colour_count)]
        colour_index = 0

        while True:
            time.sleep(1)
            colour_index = (colour_index + 1) % len(colours)
            await client.edit_role(flash_server, flash_role, colour=colours[colour_index])
            print(colour_index)

client.run(bot_token)