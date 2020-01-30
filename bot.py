import discord
import time
import asyncio
import youtube_dl


#id= 62064********13889
messages = joined = 0


def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


token = read_token()

client = discord.Client()


async def update_stats():
    await client.wait_until_ready()
    global messages, joined
    while not client.is_closed():
        try:
            with open("stats.txt", "a") as f:
                f.write(f"Time:{int(time.time())},Messages:{messages},Members Joined:{joined} \n")
            messages = 0
            joined = 0

            await asyncio.sleep(5)

        except Exception as e:
            print(e)
            await asyncio.sleep(5)


@client.event
async def on_ready():
    print("Bot online.")


@client.event
async def on_member_update(before, after):
    n = after.nick
    if n:
        if n.lower().count("techwithsunny") > 0:
            last = before.nick
            if last:
                await after.edit(nick=last)
            else:
                await after.edit(nick="NO STOP THAT")


@client.event
async def on_member_join(member):
    global joined
    joined += 1
    for channel in member.server.channels:
        if str(channel) == "general":
            await client.send_message(f"""Welcome to the Server{member.mention}""")


@client.event
async def on_message(message):
    global messages
    messages += 1
    id1 = client.get_guild(620647584226213889)
    channels = ["commands"]
    bad_words = ["bad", "stop", "69"]
    for word in bad_words:
        if message.content.count(word) > 0:
            print("A bad word was said")
            await message.channel.purge(limit=1)
    if message.content == "!help":
        embed = discord.Embed(title="Help on BOT", description="some useful commands")
        embed.add_field(name="!hello", value="Greets the user")
        embed.add_field(name="!users", value="Prints number of users")
        await message.channel.send(content=None, embed=embed)
    if message.content.find("Hello") != -1:
        await message.channel.send("Hi")
    if message.content.find("What is your name?") != -1:
        await message.channel.send("My name is sunny BOT")
    if message.content.find("Who is your creator?") != -1:
        await message.channel.send("Sunyul Hossen is my creator")
    if message.content.find("Where were you created?") != -1:
        await message.channel.send("I was created in a town named NAIHATI which is in WEST BENGAL, INDIA")
    if message.content.find("What are your future plans?") != -1:
        await message.channel.send("I would like to communicate in voice chat, and even i would love to play songs and videos from youtube on your command and finally but not the least i would love to interact with you like my brother GOOGLE ASSISTANT at some time of my life, thank you")
    if message.content.find("Who is your love?") != -1:
        await message.channel.send("I love you all")
    if message.content.find("Explain yourself") != -1:
        await message.channel.send("I am a chat bot created by Sunyul Hossen, i was created on 8th of september 2019 and im here to interact with you! if you feel lonely just send a hello and i will be there in no time! Thank YOU")
    if message.content.find("What can you do?") != -1:
        await message.channel.send("I am a chat bot, i im here to interact with you! I have answers to some of your questions, but i can asnwer a limited number of your questions supplied to me by my creator Sunyul Hossen! i would like to have a voice input prompt soon into my profile and would interact vocally with you! but since im new i need some time for my upgradation!Thank YOU")
    elif message.content == "users":
        await message.channel.send(f"""# of members: {id1.member_count}""")
    else:
        print(f"""User:{message.author} tried to do command {message.content}""")


@client.event
async def on_reaction_add(reaction, user):
    channel = reaction.message.channel
    await client.send_message(channel, '{} added {} to: {}'.format(user.name, reaction.emoji, reaction.message.content))


@client.event
async def on_reaction_remove(reaction, user):
    channel = reaction.message.channel
    await client.send_message(channel, '{} removed {} from: {}'.format(user.name, reaction.emoji, reaction.message.content))

client.loop.create_task(update_stats())

client.run(token)



