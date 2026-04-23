import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
load_dotenv()

print("Lancement du bot...")
bot = commands.Bot(command_prefix:="!", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot allumé !")
    try:
        synced = await bot.tree.sync()
        print(f"Commandes slash synchronisées : {len(synced)}")
    except Exception as e:
        print(e)

@bot.event
async def on_message(message: discord.Message):
    if message.author.bot:
        return

    if message.content.lower() == 'bonjour':
        channel = message.channel
        author = message.author
        await author.send("Comment tu vas ?")
    if message.content.lower() == "bienvenue":
        welcome_channel = bot.get_channel(1496869606088900769)
        await welcome_channel.send("Bienvenue")

@bot.tree.command(name="test", description="Tester les embeds")
async def test(interaction: discord.Interaction):
    embed = discord.Embed(
        title="Test Title",
        description="Description de l'embed",
        color=discord.Color.green()
    )
    embed.add_field(name="Généalogie", value="Suivez votre généalogie", inline=False)
    embed.add_field(name="Histoire", value="Découvrez l'histoire à travers des mini-jeux", inline=False)
    embed.set_footer(text="Pied de page")

    await interaction.response.send_message(embed=embed)


@bot.tree.command(name="warnguy", description="Alerter une personne")
async def warnguy(interaction: discord.Interaction, member: discord.Member):
    await interaction.response.send_message("Alerte envoyée !")
    await member.send("Tu as reçu un avertissement !")

@bot.tree.command(name="banguy", description="Bannir une personne")
async def banguy(interaction: discord.Interaction, member: discord.Member):
    await interaction.response.send_message("Ban envoyée !")
    await member.ban(reason="Tu n'as pas respecté le réglement du serveur.")
    await member.send("Tu as été banni !")

@bot.tree.command(name="invit_discord", description="Affiche un lien d'invitation pour Discord")
async def invit_discord(interaction: discord.Interaction):
    await interaction.response.send_message("Invite de nouveau utilisateurs : https://discord.gg/zX5Axmw9mz")

bot.run(os.getenv('DISCORD_TOKEN'))