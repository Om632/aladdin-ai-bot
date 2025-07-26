import discord
from discord.ext import commands
import os
import openai
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")
OPENAI_KEY = os.getenv("OPENAI_API_KEY")

openai.api_key = OPENAI_KEY

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"🟢 Logged in as {bot.user}")

@bot.command()
async def advice(ctx, *, query):
    """Ask for investment advice"""
    await ctx.send("🧠 Thinking...")

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are a financial assistant. Give clear and smart investment advice."},
                  {"role": "user", "content": query}]
    )
    reply = response.choices[0].message["content"]
    await ctx.send(f"📊 Investment Advice:\n{reply}")

@bot.command()
async def budget(ctx, amount: str):
    await ctx.send(f"✅ Budget set to {amount}. I’ll help you invest smartly.")

# You can add more commands like !track STOCK or !gold etc.

bot.run(TOKEN)
