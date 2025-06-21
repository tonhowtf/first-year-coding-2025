import discord
from discord.ext import commands
from discord import app_commands
import random
import os
import json


from decouple import config

id = discord.Object(id=1368715022896861236)


image = "https://img.pokemondb.net/sprites/home/normal/2x/avif/bulbasaur.avif"

image2 = "https://img.pokemondb.net/sprites/home/normal/2x/avif/ivysaur.avif"

image3 = "https://img.pokemondb.net/sprites/home/normal/2x/avif/venusaur.avif"

TOKEN = config('API')

class MeuClient(discord.Client):
    def __init__(self,*,intents:discord.Intents):
        super().__init__(intents=intents,application_id=1386033123116060853)
        self.tree = app_commands.CommandTree(self)
    
    async def setup_hook(self):
        self.tree.copy_global_to(guild=id)
        await self.tree.sync(guild=id)

client = MeuClient(intents=discord.Intents.default())


@client.event
async def on_ready():
    print('Ligado')

@client.tree.command()
async def ola(interaction: discord.Interaction):
    await interaction.response.send_message('Olá')

@client.tree.command()
async def embed(interaction: discord.Interaction):
    embed = discord.Embed(
        title = "Embed",
        description = "Descrição do embed",
        colour=14707394
    )

    embed.set_author(name="Author", icon_url=image)
    embed.set_thumbnail(url=image2)
    embed.set_image(url=image3)
    embed.set_footer(text="Footer")

    embed.add_field(name="Nome 1", value="campo 1", inline=False)
    embed.add_field(name="Nome 2", value="campo 1", inline=False)
    embed.add_field(name="Nome 3", value="campo 1", inline=False)
    embed.add_field(name="Nome 4", value="campo 1", inline=True)
    embed.add_field(name="Nome 5", value="campo 1", inline=True)


    await interaction.response.send_message(embed=embed)

@client.tree.command()
async def dado(interaction: discord.Interaction):

    numero = random.randint(1,6)
    await interaction.response.send_message(f"Você rolou um dado e caiu o número {dado}")

@client.tree.command()
async def usuario(interaction: discord.Interaction, usuario: discord.Member):
    
    await usuario.edit(nick="Pedro")

@client.tree.command()
@app_commands.default_permissions(kick_members=True)
async def expulsar(interaction: discord.Interaction, usuario: discord.Member, motivo: str = ""):
    try:
        await usuario.kick(reason=motivo)
    except:
        await interaction.response.send_message('Usuario não foi expulso')

@client.tree.command()
@app_commands.default_permissions(manage_messages=True)
async def limparchat(interaction:discord.Interaction, quantidade:int):
    await interaction.channel.purge(limit=quantidade)
    await interaction.response.send_message('Apagado com sucesso')

@client.tree.command()
async def criarticket(interaction:discord.Interaction):

    atendente = interaction.guild.get_role(1386105628375646369)
    categoria = interaction.guild.get_channel(1386106829343297586)

    overwrites = {
        interaction.guild.default_role: discord.PermissionOverwrite(view_channel=False),
        interaction.guild.me: discord.PermissionOverwrite(view_channel=True),
        atendente: discord.PermissionOverwrite(view_channel=True),
        interaction.user: discord.PermissionOverwrite(view_channel=True)

    }

    canal = await interaction.guild.create_text_channel(f"ticket-{interaction.user.name}", overwrites=overwrites, category=categoria)
    await interaction.response.send_message(f'O atendimento foi criado em {canal.mention}', ephemeral=True)
    await canal.send(f'{interaction.user.mention} você abriu um atendimento!')

@client.tree.command()
async def apagarticket(interaction:discord.Interaction):
    await interaction.channel.delete()

#Definindo a função de visualizar a carteira
async def mostrar_carteira():
    with open('carteira.json', 'r') as f:
        saldos = json.load(f)
    
    return saldos

async def abrir_conta(user):
    saldos = await mostrar_carteira()

    if str(user.id) in saldos:
        return False
    else:
        saldos[str(user.id)] = {}
        saldos[str(user.id)]["saldo"] = 0
    
    with open("carteira.json", "w") as f:
        json.dump(saldos, f)
    return True

async def adicionar_saldo(user, valor):
    await abrir_conta(user)
    saldos = await mostrar_carteira()
    saldos[str(user.id)]['saldo'] += int(valor)

    with open('carteira.json', 'w') as f:
        json.dump(saldos, f)
    
    return saldos[str(user.id)]["saldo"]

@client.tree.command()
async def adicionarsaldo(interaction:discord.Interaction,quantidade:int, membro:discord.Member=None):
    if membro == None:
        membro = interaction.user
    
    await adicionar_saldo(membro, quantidade)

    await interaction.response.send_message(f"O usuário recebeu {quantidade} de moedas", ephemeral=True)


@client.tree.command()
async def saldo(interaction:discord.Interaction, membro:discord.Member=None):
    if membro == None:
        membro = interaction.user
    
    await abrir_conta(membro)
    saldos = await mostrar_carteira()
    dinheiro = saldos[str(membro.id)]["saldo"]

    await interaction.response.send_message(f"O usuário tem {dinheiro} de dinheiro", ephemeral=True)

client.run(TOKEN)
