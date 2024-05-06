import discord
import random
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))


sad_words = ["depressed", "sad", "miserable", "tired", "anxious", "angry"]
encouragements = [
  "Don't worry! You can overcome it!",
  "All will pass, cheer up",
  "You're a great person man, cmon",
  "Stay strong my brother!",
  "Once the journey has started, there is no going back..."
]
victory_words = ["happy", "won", "glad", "excited", "satisfied", "great"]
hype = [
  "See? You could do it after all!",
  "Keep it up man!",
  "Lets go for more man",
  "Yeah at it buddy!",
  "I'm proud of you"
]
songs = ["https://youtu.be/3WpdCZC9q6w?si=7q3lzQY9pJk8-Buo", "https://youtu.be/Ej8RhiSv2-4?si=Q7uJTssZHppKT3Of", 
         "https://youtu.be/W-w3WfgpcGg?si=jy0DJvkp-9u4Tc3q"]
random_song = random.choice(songs)
@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith("!hi"):
    await message.channel.send(f"hello bro")
  if message.content.startswith("w!gif"):
    await message.channel.send(f"https://media.giphy.com/media/duNowzaVje6Di3hnOu/giphy.gif?cid=790b7611k0f18pqtlo0j4or65mdtx7merm1jrgihn2n015wi&ep=v1_gifs_trending&rid=giphy.gif&ct=g")
  if message.content.startswith("!song"):
    await message.channel.send(random_song)
  if any(word in message.content for word in sad_words):
    response = random.choice(encouragements)
    await message.channel.send(response)
  if any(word in message.content for word in victory_words):
    response = random.choice(hype)
    await message.channel.send(response)
client.run("MTIxMTY1MDE0MzI1NTAwMzE0Ng.GyZIZ_.EWB_x4AMYQoLCxZY2eYoQ24d0OJXF1dGe4_3J0", reconnect=True)



