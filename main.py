import discord #importing discord
import os
import random       #just a lib to get get random number from a specific range
TOKEN='FAKETOKEN192930291 BECAUSE I DON\'T WANT YOU TO USE MY BOT HEH'      #we get the token while building bot in discord devloper portal
intent=discord.Intents.default()
intent.members=True
intent.message_content=True
client=discord.Client(intents=intent)
@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))           #login to the bot

@client.event
async def on_message(message):
    # manual responses
    username=str(message.author).split('#')[0]
    user_message=str(message.content)
    channel=str(message.channel.name)
    print(f'{username}:{user_message} ({channel})')

    if message.author ==client.user:
        return

    if message.channel.name=='general':
        if user_message.lower()=='bye':
            await message.channel.send(f'you are not welcomed here anyways!! ๐นโฟ๐น')
            return
        elif user_message.lower() == "bean lucky number":
            response=f'your lucky number is {random.randrange(10)}. '
            await message.channel.send(response)

    if user_message.lower()=='bean anywhere':
        await message.channel.send('used anywhere but here!')
        return


    if user_message.lower() == 'hello' or user_message.lower() == 'hey' or user_message.lower() == 'hlo' or user_message.lower() == 'heya':
        await message.channel.send(f'NAMASTE!!')
        return


client.run(TOKEN)
