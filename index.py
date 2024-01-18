#BOT DISCORD CREE PAR SP1D3R
import discord
from discord.ext import commands, tasks 
import requests
import random
from inspect import CO_NESTED
from typing import Literal
from discord.ext import commands
import discord
import youtube_dl
import asyncio
import json
import openai 
import string 
import re 
import os
from pypresence import Presence
import time
import subprocess
from dotenv import load_dotenv
intents = discord.Intents.all()
intents.presences = True  # Activer les intents de présence
intents.typing = False  # Vous pouvez activer les autres intents si nécessaire

# Préfixe pour les commandes du bot
bot  = commands.Bot(command_prefix = '!',intents = intents)

#RPC
@bot.event
async def on_ready():
    print(f'Connecté en tant que {bot.user.name}')
    await update_rpc_status.start()

@tasks.loop(seconds=60)
async def update_rpc_status():
    activity = discord.Activity(
        type=discord.ActivityType.playing, 
        name="FyShop"
    )

    await bot.change_presence(activity=activity)

    rpc_messages = [
        "💬・CryptChat @2023",
        "🔒・Anonyme Chat",
        "🎮・FIVEM",
        "👨‍🔬・DARKCHAT",
        "🐦・TWITTER",
    ]

    # Mettez à jour la RPC lors du démarrage
    await update_rpc(rpc_messages)

@tasks.loop(seconds=5)  # Mettez à jour la RPC toutes les 5 secondes
async def update_rpc(rpc_messages):
    if not hasattr(update_rpc, "counter"):
        update_rpc.counter = 0  # Initialiser le compteur

    message = rpc_messages[update_rpc.counter]
    update_rpc.counter = (update_rpc.counter + 1) % len(rpc_messages)

    activity = discord.Activity(
        name=message,
        type=discord.ActivityType.watching
    )

    await bot.change_presence(activity=activity)

# Démarrer la boucle de mise à jour de la RPC
@bot.event
async def on_connect():
    await asyncio.sleep(1)  # Attendre un court instant pour que l'event loop soit prêt

    # Définir les messages à afficher dans la RPC
    rpc_messages = [
        "💬・CryptChat @2023",
        "🔒・Anonyme Chat",
        "🎮・FIVEM",
        "👨‍🔬・DARKCHAT",
        "🐦・TWITTER",
    ]
    
    update_rpc.start(rpc_messages)


#ano 



@bot.command()
async def shutdown(ctx):
    await bot.close()

@bot.command(name="ano")
async def ano(ctx, *, text):
    
    await ctx.message.delete()
    embed = discord.Embed(description=text, color=0x000000)
    embed.set_author(name="🕵️ Message DarkChat")
    embed.set_footer(text="CryptChat @2023")
    await ctx.send(embed=embed)
    if len(ctx.message.attachments) == 0:
        return
    image_url = ctx.message.attachments[0].url
    embed = discord.Embed()
    embed.set_image(url=image_url)
    await ctx.send(embed=embed)

    




    # Commande d'aide
@bot.command(name='aide')  # Utilisez 'name' pour définir le nom de la commande
async def aide(ctx):
    embed = discord.Embed(title="💬 CryptChat - Aide", description="Voici la liste des commandes disponibles :")

    # Ajoutez des champs pour chaque commande
    embed.add_field(name="!ano", value="Cette commande permet d'écrire anonymement.", inline=False)
    embed.add_field(name="!twt", value="Cette commande permet d'écrire sur twitter.", inline=False)
    embed.add_field(name="!ticket ", value="Cette commande permet d'ouvrir un ticket et contacter le support", inline=False)
    embed.add_field(name="!loto", value="Cette commande permet de jouer au loto.", inline=False)
    embed.add_field(name="!suggestion", value="Cette commande permet de proposé des suggestions pour le serveur.", inline=False)
    embed.add_field(name="!say ", value="Cette commande permet d'envoyer un message avec le bot.", inline=False)
    embed.add_field(name="!mod ", value="Cette commande permet de voir toutes les commandes de modération.", inline=False)
    embed.add_field(name="!demask (id) ", value="(En Développement) Cette commande permet de voir l'identifiant de l'utilsateur qui à envoyer un message sur le darkchat.", inline=False)
    embed.add_field(name="!info ", value="Cette commande permet de voir le status du serveur", inline=False)
    embed.add_field(name="!clear ", value="Cette commande permet d'effacer le nom de message inscrit", inline=False)
    embed.add_field(name="!renew ", value="Cette commande permet de nettoyer le salon souhaité", inline=False)
    embed.set_footer(text="www.cryptchat.fr")
    await ctx.message.delete()

    # Vous pouvez ajouter autant de champs que nécessaire

    await ctx.send(embed=embed)


@bot.command()
async def renew(ctx):
    # Vérifier si l'utilisateur a les autorisations nécessaires
    if ctx.author.guild_permissions.administrator:
        channel = ctx.channel

        # Effacer le chat
        await channel.purge()

        # Réinitialiser le salon en supprimant tous les messages épinglés
        pinned_messages = await channel.pins()
        for message in pinned_messages:
            await message.unpin()

        # Envoyer un message pour indiquer que le salon a été réinitialisé
        await channel.send("💬 CryptChat à reinisialisé le salon !")

    else:
        await ctx.send("Désolé, vous n'avez pas les autorisations nécessaires pour utiliser cette commande.")

@bot.command()

async def twt(ctx, *, text):
    await ctx.message.delete()
    embed = discord.Embed(description=text, color=0x6fa8dc)
    embed.set_author(name="🐦 Message Twitter")
    embed.set_footer(text="CryptChat @2023")
    await ctx.send(embed=embed)
    await ctx.message.delete()

#LOGS DISCORD : 

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith("!ano"):
        logs_channel = bot.get_channel(1147189191600517170) 
        await logs_channel.send(f"🕵️ CryptChat DARKCHAT - Commande !ano utilisée par {message.author}: {message.content}")
    await bot.process_commands(message)




    if message.content.startswith("!twt"):
        logs_channel = bot.get_channel(1147189191600517170) 
        await logs_channel.send(f"🐦 CryptChat TWT - Commande !twt utilisée par {message.author}: {message.content}")
    await bot.process_commands(message)

#DEMASK : 

@bot.command()
async def demask(ctx, message_id: int):
    if ctx.author.guild_permissions.administrator:
        await ctx.send(message)
    else:
        await ctx.send("Vous devez être administrateur pour utiliser cette commande.")
    await ctx.message.delete()
    try:
        message = await ctx.channel.fetch_message(message_id)
        
        if message:
            author_id = message.author.id
            await ctx.send(f"🕵️ L'identifiant Discord de l'auteur du message est : {author_id}")
        else:
            await ctx.send("Message introuvable.")
    except discord.NotFound:
        await ctx.send("Message introuvable.")
               # Votre code de gestion des messages ici
    except Exception as e:
        print(f"Ignoring exception in on_message: {e}")

        #SUGGES
@bot.event
async def on_message(message):
    # Ignorer les messages du bot pour éviter les boucles infinies
    if message.author == bot.user:
        return

    # Supprimer les messages qui ne commencent pas par la commande !suggestion
    if not message.content.startswith('!suggestion '):
        await message.delete()
        return

    # Laisser le message passer pour être traité par les commandes
    await bot.process_commands(message)

@bot.command()
async def suggestion(ctx, *, message):
    # Supprimer le message d'origine de l'utilisateur
    await ctx.message.delete()

    # Trouver le salon pour les suggestions par son ID
    suggestion_channel = ctx.guild.get_channel(1152679831566286958)
    
    if suggestion_channel is not None:
        # Créer un embed pour la suggestion
        embed = discord.Embed(
            title="Nouvelle Suggestion",
            description=message,
            color=discord.Color.blue()
        )
        embed.add_field(name="🧑 - Proposé par", value=ctx.author.mention, inline=False)
        
        # Envoyer l'embed dans le salon de suggestions
        suggestion_message = await suggestion_channel.send(embed=embed)
        
        # Ajouter les réactions "oui" et "non" automatiquement
        await suggestion_message.add_reaction("✅")  # Emoji pour "oui"
        await suggestion_message.add_reaction("❌")  # Emoji pour "non"
    else:
        await ctx.send("Le salon de suggestions n'a pas été trouvé. Veuillez vérifier l'ID du salon dans le code.")
        

        

#SERVEUR FIVEM 
@bot.command()
async def info(ctx):
    # Vérifiez si le serveur FiveM est en ligne
    SERVER_IP = '5.135.172.146'
    server_status = get_server_status(SERVER_IP)

    if server_status['online']:
        player_count = server_status['players']
        last_reboot = server_status['last_reboot']
        players_today = server_status['players_today']

        embed = discord.Embed(title="Informations sur le serveur FiveM",
                              color=discord.Color.green())
        embed.add_field(name="Statut du serveur", value="En ligne", inline=False)
        embed.add_field(name="Nombre de joueurs en ligne", value=f"{player_count} joueur(s)", inline=False)
        embed.add_field(name="Dernier redémarrage", value=last_reboot, inline=False)
        embed.add_field(name="Joueurs connectés aujourd'hui", value=f"{players_today} joueur(s)", inline=False)

    else:
        embed = discord.Embed(title="Informations sur le serveur FiveM",
                              color=discord.Color.red())
        embed.add_field(name="Statut du serveur", value="Hors ligne", inline=False)

    await ctx.send(embed=embed)

def get_server_status(server_ip):
    try:
        response = requests.get(f"")
        data = response.json()

        if data:
            status = {
                "online": True,
                "players": data.get("players", 0),
                "last_reboot": data.get("last_reboot", "Inconnu"),
                "players_today": data.get("players_today", 0),
            }
        else:
            status = {"online": False}

    except Exception as e:
        print(f"Une erreur s'est produite lors de la récupération des informations du serveur : {str(e)}")
        status = {"online": False}

    return status
#ADMIN 


@bot.command()
async def supp(ctx, message_id):
    # Vérifiez si l'auteur de la commande est un administrateur du serveur
    if ctx.author.guild_permissions.administrator:
        try:
            message = await ctx.channel.fetch_message(int(message_id))
            await message.delete()
            await ctx.send(f"Message {message_id} supprimé avec succès.")
        except discord.NotFound:
            await ctx.send("Message introuvable.")
        except Exception as e:
            await ctx.send(f"Une erreur s'est produite : {str(e)}")


#MESSAGE DE BIENVENUE 

@bot.event
async def on_member_join(member):
    # Récupère le salon où envoyer le message de bienvenue
    welcome_channel = discord.utils.get(member.guild.text_channels, name="bienvenue")

    if welcome_channel:
        # Envoie le message de bienvenue avec mention de l'utilisateur
        await welcome_channel.send(f'👨‍🎓️ Bienvenue {member.mention} sur le serveur ! Utilise la commande !aide')
         
         #COMMANDE !SAY

         # Fonction pour répondre à la commande !say
@bot.command()
async def say(ctx, *, message):
    await ctx.send(message)
    await ctx.message.delete()


    #MODERATION : 

@bot.command()
async def mod(ctx):
    await ctx.message.delete()
    mod_embed = discord.Embed(title='Commandes de Modération',
                              description='Liste des commandes de modération disponibles :',
                              color=discord.Color.blue())
    

    mod_embed.add_field(name='!kick [utilisateur]', value='Expulse un utilisateur du serveur.')
    mod_embed.add_field(name='!ban [utilisateur]', value='Bannit un utilisateur du serveur.')
    mod_embed.add_field(name='!mute [utilisateur]', value='Rend un utilisateur muet dans le salon actuel.')
    mod_embed.add_field(name='!unmute [utilisateur]', value='Définit la parole libre pour un utilisateur muet.')
    mod_embed.add_field(name='!clear [nombre]', value='Supprime un certain nombre de messages dans le salon.')
    mod_embed.add_field(name='!role on ou !role off', value='Pour activer ou désactiver lautorôle quand un membre rejoins le serveur')
    mod_embed.add_field(name='!say', value='Pour envoyer un message avec le bot CryptChat')
    
    await ctx.send(embed=mod_embed)
    
@bot.command()
async def kick(ctx, member: discord.Member, *, reason=None):
    if ctx.author.guild_permissions.kick_members:
        await member.kick(reason=reason)
        await ctx.send(f'{member.mention} a été expulsé du serveur.')
    else:
        await ctx.send("Vous n'avez pas les autorisations nécessaires pour exécuter cette commande.")

@bot.command()
async def ban(ctx, member: discord.Member, *, reason=None):
    if ctx.author.guild_permissions.ban_members:
        await member.ban(reason=reason)
        await ctx.send(f'{member.mention} a été banni du serveur.')
    else:
        await ctx.send("Vous n'avez pas les autorisations nécessaires pour exécuter cette commande.")

@bot.command()
async def mute(ctx, member: discord.Member):
    if ctx.author.guild_permissions.manage_roles:
        muted_role = discord.utils.get(ctx.guild.roles, name="Muted")
        if not muted_role:
            muted_role = await ctx.guild.create_role(name="Muted")
            for channel in ctx.guild.text_channels:
                await channel.set_permissions(muted_role, send_messages=False)
        await member.add_roles(muted_role)
        await ctx.send(f'{member.mention} a été rendu muet dans le salon actuel.')
    else:
        await ctx.send("Vous n'avez pas les autorisations nécessaires pour exécuter cette commande.")

@bot.command()
async def clear(ctx, amount: int):
    if ctx.author.guild_permissions.manage_messages:
        await ctx.channel.purge(limit=amount + 1)  # +1 to account for the command message
        await ctx.send(f'{amount} messages ont été supprimés dans ce salon.', delete_after=1)
    else:
        await ctx.send("Vous n'avez pas les autorisations nécessaires pour exécuter cette commande.")

#DISCORD SUPP :
                
    
                # Supprimez le message du bot dans le salon où il a été envoy

@bot.command()
async def upload(ctx):
    # Vérifie que la commande a un fichier joint (image ou vidéo)
    if len(ctx.message.attachments) == 0:
        await ctx.send("Veuillez joindre une vidéo ou une image avec votre message.")
        return

    # Récupère le premier fichier joint
    attachment = ctx.message.attachments[0]

    # Vérifie que le fichier est une image ou une vidéo
    if not attachment.filename.endswith(('.jpg', '.jpeg', '.png', '.gif', '.mp4', '.mov')):
        await ctx.send("Le fichier joint doit être une image (jpg, jpeg, png, gif) ou une vidéo (mp4, mov).")
        return

    # Envoie le fichier joint avec le message du bot
    await ctx.send(f"Message de {ctx.author.display_name} :")
    await ctx.send(file=await attachment.to_file())

#AUTOROLE : 

# ID du rôle à attribuer
role_id = 1147527661632094278

@bot.event
async def on_ready():
    print(f'Connecté en tant que {bot.user.name}')

@bot.command()
async def role(ctx, action):
    # Vérifiez si l'utilisateur a les autorisations nécessaires pour effectuer cette action
    if not ctx.author.guild_permissions.manage_roles:
        await ctx.send("Vous n'avez pas la permission de gérer les rôles.")
        return
    
    # Obtenez le rôle en fonction de l'ID
    role = ctx.guild.get_role(role_id)

    if action == 'on':
        # Attribuez le rôle à l'utilisateur
        await ctx.author.add_roles(role)
        await ctx.send(f"Vous avez maintenant le rôle {role.name}.")
    elif action == 'off':
        # Retirez le rôle de l'utilisateur
        await ctx.author.remove_roles(role)
        await ctx.send(f"Vous n'avez plus le rôle {role.name}.")
    else:
        await ctx.send("Utilisation incorrecte de la commande !role. Utilisez !role on ou !role off.")

# ID du rôle à attribuer
role_id = 1147527661632094278

@bot.event
async def on_ready():
    print(f'Connecté en tant que {bot.user.name}')

@bot.event
async def on_member_join(member):
    # Obtenez le serveur (guild) du membre
    guild = member.guild

    # Obtenez le rôle en fonction de l'ID
    role = discord.utils.get(guild.roles, id=role_id)

    if role is not None:
        # Attribuez le rôle au membre
        await member.add_roles(role)
        print(f"Le rôle {role.name} a été attribué à {member.display_name}.")


 #CRYPTIA




#PING 


@bot.event
async def on_message(message):
    # Vérifiez si le message contient une mention du bot
    if bot.user.mentioned_in(message):
        embed = discord.Embed(
            title="Hey, je suis là, ne t'inquiète pas !",
            description="Utilise la commande !aide pour plus d'informations.",
            color=discord.Color.green()
        )
        embed.set_footer(text="www.cryptchat.fr")

        # Répondez avec l'embed
        await message.channel.send(embed=embed)

    await bot.process_commands(message)


#VERIF 


# Définir une variable pour suivre si la vérification est activée ou désactivée
verification_active = False

@bot.command()
async def verif(ctx):
    global verification_active
    
    # Vérifier si la vérification est déjà activée
    if verification_active:
        await ctx.send("La vérification est déjà activée.")
    else:
        await ctx.send("Vérification activée. Répondez au captcha suivant pour vous vérifier.")
        await ctx.send(embed=generate_captcha_embed())
        verification_active = True

@bot.command()
async def verif_off(ctx):
    global verification_active
    
    # Vérifier si la vérification est déjà désactivée
    if not verification_active:
        await ctx.send("La vérification est déjà désactivée.")
    else:
        await ctx.send("Vérification désactivée.")
        verification_active = False

def generate_captcha_embed():
    # Génération d'un captcha (exemple simple ici)
    captcha_characters = string.ascii_uppercase + string.digits + "!@#$%^&*()_+-=[]{}|;:,.<>?"
    captcha_text = ''.join(random.choices('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890', k=6))
    
    embed = discord.Embed(title="Captcha", description="Résolvez le captcha suivant pour vous vérifier.")
    embed.add_field(name="Captcha Text", value=captcha_text, inline=False)
    
    return embed

@bot.event
async def on_message(message):
    global verification_active
    
    if message.author == bot.user:
        return
    
    if verification_active and message.content.upper() == 'CAPTCHA':
        await message.author.send("Félicitations ! Vous avez résolu le captcha.")
        await message.author.add_roles(message.guild.get_role(1148713739118452839))  # Remplacez ROLE_ID_HERE par l'ID du rôle de vérification
        verification_active = False

    await bot.process_commands(message)



intents = discord.Intents.default()
intents.typing = False
intents.presences = False


role_non_verifie_id = 1148715455633178704  # Remplacez par l'ID du rôle "Non vérifié"
role_verifie_id = 1148713739118452839  # Remplacez par l'ID du rôle "Vérifié"

# Définir une variable pour suivre si la vérification est activée ou désactivée
verification_active = False


#loto 

# Dictionnaire pour stocker l'argent des utilisateurs
argent_utilisateurs = {}

# Liste des prix de la loterie
prix_loterie = ["100,000$ IG", "50,000$", "10,000$", "5,000$", "2,000$"]

# Liste des numéros aléatoires
numeros_aleatoires = []

@bot.event
async def on_ready():
    print(f'Connecté en tant que {bot.user.name}')

@bot.command(name='money')
async def money(ctx):
    if ctx.author.id not in argent_utilisateurs:
        argent_utilisateurs[ctx.author.id] = 0

    solde = argent_utilisateurs[ctx.author.id]
    await ctx.send(f"{ctx.author.mention}, votre solde d'argent loto est de {solde}$.")

@bot.command(name='give')
async def give(ctx, user: discord.User, montant: int):
    if ctx.message.author.id != 1146715605647503400:  # Remplacez VOTRE_ID_ADMIN par l'ID de l'administrateur
        await ctx.send("Seuls les administrateurs peuvent utiliser cette commande.")
        return

    if user.id not in argent_utilisateurs:
        argent_utilisateurs[user.id] = 0

    # Vérifiez si montant est un entier valide
    if not isinstance(montant, int):
        await ctx.send("Veuillez spécifier un montant valide en tant qu'entier.")
        return

    # Vérifiez que le solde ne devient pas négatif
    if montant < 0 and argent_utilisateurs[user.id] + montant < 0:
        await ctx.send(f"{user.mention} n'a pas suffisamment d'argent pour effectuer cette opération.")
        return

    argent_utilisateurs[user.id] += montant

    if montant >= 0:
        operation = "donné"
    else:
        operation = "retiré"

    await ctx.send(f"{ctx.author.mention} a {operation} {abs(montant)}$ à {user.mention}. Le solde actuel de {user.mention} est de {argent_utilisateurs[user.id]}$.")

@bot.command(name='loto')
async def loto(ctx, mise: int = 0):
    if mise <= 0:
        await ctx.send("Veuillez spécifier une mise valide supérieure à zéro, par exemple : `!loto 100`.")
        return

    # Générer un numéro de loterie aléatoire
    numero_gagnant = random.choice(prix_loterie)

    # Créer un embed avec l'image de la loterie
    embed = discord.Embed(title="Loterie", description="Achetez un billet de loterie pour avoir une chance de gagner !", color=0xffd700)
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1147528054634197033/1152671045929680916/Loto-noel.jpg")  # Remplacez par l'URL de votre image de loterie

    # Ajouter les prix disponibles dans l'embed
    for prix in prix_loterie:
        embed.add_field(name="Prix", value=prix, inline=False)

    # Envoyer l'embed dans le canal Discord
    message = await ctx.send(embed=embed)

    # Attendre quelques secondes
    await asyncio.sleep(5)

    # Sélectionnez 5 numéros aléatoires de 1 à 50
    numeros_aleatoires = random.sample(range(1, 51), 5)

    # Vérifiez si les numéros correspondent aux numéros gagnants
    if random.random() < 0.1:  # 10% de chance de gagner
        gagnant = True
        prix_gagne = numero_gagnant
        argent_utilisateurs[ctx.author.id] += mise * 2  # Le joueur gagne le double de sa mise
    else:
        gagnant = False
        prix_gagne = "Rien"
        argent_utilisateurs[ctx.author.id] -= mise

    # Envoyez un message pour annoncer le résultat
    if gagnant:
        await ctx.send(f"Félicitations à {ctx.author.mention} ! Vous avez gagné {prix_gagne} en misant {mise}$. Votre solde actuel est de {argent_utilisateurs[ctx.author.id]}$.")
    else:
        await ctx.send(f"Dommage, {ctx.author.mention}. Vous avez misé {mise}$, mais vous n'avez rien gagné cette fois. Votre solde actuel est de {argent_utilisateurs[ctx.author.id]}$.")

@bot.command(name='listenum')
async def listenum(ctx):
    if not numeros_aleatoires:
        numeros_aleatoires = random.sample(range(1, 51), 5)

    embed = discord.Embed(title="Liste des Numéros Aléatoires", color=0x00ff00)
    embed.add_field(name="Numéros", value=", ".join(map(str, numeros_aleatoires)), inline=False)

    await ctx.send(embed=embed)


#ANNONCE

# Variables pour gérer l'état de l'annonce
annonce_active = True
annonce_channel_id = None  # ID du salon où les annonces seront diffusées

# Message d'annonce
annonce_message = "Annonce importante : Il y a une mise à jour du serveur !"

@bot.event
async def on_ready():
    print(f'Connecté en tant que {bot.user.name}')
    # Démarrez la tâche de diffusion automatique d'annonces si elle est active
    if annonce_active:
        annonce_loop.start()

@tasks.loop(hours=24)  # Diffusez une annonce toutes les 24 heures (vous pouvez ajuster ceci)
async def annonce_loop():
    # Récupérez le salon d'annonce par son ID
    annonce_channel = bot.get_channel(annonce_channel_id)
    
    if annonce_channel:
        await annonce_channel.send(annonce_message)

@bot.command()
async def annonce(ctx, state: str):
    global annonce_active
    if state.lower() == "on":
        annonce_active = True
        await ctx.send("Annonces activées.")
        annonce_loop.start()
    elif state.lower() == "off":
        annonce_active = False
        await ctx.send("Annonces désactivées.")
        annonce_loop.cancel()
    else:
        await ctx.send("Utilisation incorrecte. Utilisez !annonce on ou !annonce off.")

@bot.command()
async def salon(ctx, channel_id: int):
    global annonce_channel_id
    annonce_channel_id = channel_id
    await ctx.send(f"Le salon d'annonce a été défini sur <#{channel_id}>.")

@bot.command()
async def annoncecmd(ctx):
    # Créez un embed pour afficher la liste des commandes
    embed = discord.Embed(
        title="Commandes disponibles",
        description="Liste des commandes du bot",
        color=discord.Color.blue()
    )

    # Ajoutez des champs pour chaque commande
    embed.add_field(name="!annonce on/off", value="Active/Désactive les annonces automatiques.", inline=False)
    embed.add_field(name="!salon [id du salon]", value="Spécifie le salon d'annonce.", inline=False)

    # Envoyez l'embed dans le canal
    await ctx.send(embed=embed)


#SUPPORT 

@bot.command()
async def ticket(ctx):
    # Créer un canal de ticket
    category = discord.utils.get(ctx.guild.categories, name="Tickets")
    if category is None:
        overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            ctx.author: discord.PermissionOverwrite(read_messages=True),
            ctx.guild.get_role(1147549962209607763): discord.PermissionOverwrite(read_messages=True)
        }
        category = await ctx.guild.create_category(name="Tickets")
        ticket_channel = await ctx.guild.create_text_channel(name=f"ticket-{ctx.author.display_name}", category=category, overwrites=overwrites)
    else:
        overwrites = {
            ctx.guild.default_role: discord.PermissionOverwrite(read_messages=False),
            ctx.author: discord.PermissionOverwrite(read_messages=True),
            ctx.guild.get_role(1147549962209607763): discord.PermissionOverwrite(read_messages=True)
        }
        ticket_channel = await ctx.guild.create_text_channel(name=f"ticket-{ctx.author.display_name}", category=category, overwrites=overwrites)
    
    # Créer un embed pour le ticket
    embed = discord.Embed(
        title="Nouveau Ticket de Support",
        description=f"Bienvenue {ctx.author.mention}! Un membre de l'équipe de support vous assistera sous peu. Utilisez `!close` pour fermer ce ticket quand vous avez terminé.",
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1147528054634197033/1152671021590118421/Neon_Blue_and_Black_Gamer_Badge_Logo.png")
    
    # Envoyer l'embed dans le canal de ticket
    await ticket_channel.send(embed=embed)

@bot.command()
async def close(ctx):
    # Vérifier si l'auteur du message est dans un canal de ticket
    if isinstance(ctx.channel, discord.TextChannel) and ctx.channel.category is not None and ctx.channel.category.name == "Tickets":
        # Envoyer un message d'adieu sous forme d'embed au propriétaire du ticket
        embed = discord.Embed(
            title="Ticket Fermé",
            description="Merci d'avoir ouvert un ticket! En espérant avoir été utile, je vous invite donc à mettre un avis sur le serveur si vous le souhaitez.",
            color=discord.Color.green()
        )
        await ctx.author.send(embed=embed)
        
        # Supprimer le canal de ticket
        await ctx.channel.delete()
    else:
        await ctx.send("Vous ne pouvez pas utiliser cette commande en dehors d'un canal de ticket.")

# Remplacez 'YOUR_BOT_TOKEN' par le token de votre bot Discord


#SUGGESTION



# Remplacez 'YOUR_TOKEN' par le token de votre bot Discord
bot.run('MTE0NzE3MzQ2OTQxNTU1MTExNg.GWvsXq.1TZYgZRehZ4KjCAfhgnjuBvcoR6ZDgosRTo0NQ')
#NODE 