import discord
from discord import app_commands
from discord.ext import commands
import openai

# Configura tu token de API de OpenAI y de discord
OPENAI_API_KEY = "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"
DISCORD_TOKEN = "MTExNDk4MDE5NTE4NzgzMDc4NA.GKIy7t.0worWkf11Im0e_q-1rTUDRC5l6dhumTGXAzniM"

openai.api_key = OPENAI_API_KEY

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot is Up and Ready!")
    try:
        synced = await bot.tree.sync()
        print(f"Synced {len(synced)} command(s)")
    except Exception as e:
        print(e)

@bot.event
async def on_message(message):
    if message.author == bot.user:  # Ignore messages sent by the bot
        return

    # Agrega el prompt de traducción
    translation_prompt = "You're a direct, concrete, no pleasantries professional translator. You wait for the user to ask you to translate from one language to the other. You respect slang and local cultural words and phrases and translate to the appropiate cultural context in the other language"

    # Añade el mensaje del usuario al prompt de traducción
    user_message = f"{translation_prompt}\nUser: {message.content}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": user_message
            },
            {
                "role": "user",
                "content": message.content
            }
        ],
        temperature=0.5,
        max_tokens=300
    )
    # Send the response message in the same channel where the message was received
    await message.channel.send(f"Chat GPT said: {response['choices'][0]['message']['content']}")

bot.run(DISCORD_TOKEN)
