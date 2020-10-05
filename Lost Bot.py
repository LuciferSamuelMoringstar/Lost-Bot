import logging
import random
import typing
import discord
import json
import os
from discord.ext import commands, tasks

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

intents = discord.Intents.default()
intents.members = True
intents.presences = True
prefix = 'ls!'
client = commands.Bot(command_prefix=prefix, intents=intents)
client.remove_command('help')
os.chdir('C:/Users/Chris Nahimana/PycharmProjects/DiscordBot')

color = random.choice([0xAA3939, 0xDC0A0A, 0x480D99, 0xc70000])

@client.event
async def on_ready():
    change.start()
    channel = client.get_channel(762095478601941012)
    await channel.send(f"Connected to Discord as {client.user.name} #{client.user.discriminator}")
    print(f"Connected to Discord as {client.user.name} #{client.user.discriminator}")

@client.event
async def on_member_join(member):
    channel = client.get_channel(742453234618204293)
    owner = client.get_user(757003443779928196)
    if member.guild.id == 740754030623719547:
        welcome = discord.Embed(
            title=f"{str(member)} just joined the server!",
            description="ᴡᴇʟᴄᴏᴍᴇ!\n⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\nGo to <#756630275236036678> to be able to speak!\n⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\nGo to <#742973267446464564> to get roles!\n⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯⎯\nWhen you are done with all that, come chat with us here in <#742453234618204293>!",
            colour=0xFCFAFA
        )
        welcome.set_footer(text=f'Bot made by {owner}')
        await channel.send(f"{member.mention} <@&762171672865538059>")
        await channel.send(embed=welcome)
    else:
        return
    if member.guild.id == 758371378721587241:
        await member.send("Welcome to Lost Portal. This is a PM Portal so just know that you can Mass Partner. We hope you enjoy your stay here and stay forever. Well while your here also check out these cool servers. We think you should join them.\n\nEdie's Restaurant:  https://discord.gg/RaQZMge\nThe Saloon: https://discord.gg/yBMuD8h)")

@tasks.loop(seconds=300.0)
async def change():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name='for ls!help'))

@client.command()
async def profile(ctx, *, member: typing.Optional[discord.Member] = None):
    if member == None:
        member = ctx.author
    name = member.name
    nick = member.nick
    discriminator = member.discriminator
    id = member.id
    bot = member.bot
    status = member.status
    roles = ''.join([role.mention for role in member.roles])
    avatar = member.avatar_url
    created = member.created_at.__format__("%B %d, %Y %I:%M %p")
    joined = member.joined_at.__format__('%B %d, %Y %I:%M %p')
    profile = discord.Embed(
        title=f"About {name}",
        description=f"**Name:** {name}\n**Nickname:** {nick}\n**Discriminator:** {discriminator}\n**Id:** {id}\n**Bot:** {bot}\n**Status:** {status}\n**Roles:** {roles}\n**Account Created At:** {created}\n**Joined On:** {joined}",
        colour=member.top_role.colour
    )
    profile.set_thumbnail(url=avatar)
    await ctx.send(embed=profile)


@client.command()
async def server(ctx, guild: typing.Optional[int] = None):
    if guild == None:
        guild = ctx.guild
    else:
        guild = client.get_guild(guild)
    name = guild.name
    emoji = client.get_emoji(758516114148950047)
    emoji2 = client.get_emoji(758494326237298738)
    emoji3 = client.get_emoji(758516116263010314)
    emoji4 = client.get_emoji(758516115172884480)
    emoji5 = client.get_emoji(758517604259332117)
    emoji6 = client.get_emoji(758768188082094181)
    region = guild.region
    icon = guild.icon_url
    id = guild.id
    roles = guild.roles
    owner = guild.owner
    splash = guild.splash_url
    boost_level = guild.premium_tier
    boostes = guild.premium_subscription_count
    banner = guild.banner_url
    member_count = guild.member_count
    boosters = guild.premium_subscribers
    channels = guild.channels
    verification_level = guild.verification_level
    mfa_level = guild.mfa_level
    invites = await guild.invites()
    invite = ' , '.join([invite.url for invite in invites])
    created_at = guild.created_at.__format__("%B %d, %Y %I:%M %p")
    content_filter = guild.explicit_content_filter
    default_notifactions = guild.default_notifications
    features = ', '.join(guild.features)
    if mfa_level == 1:
        mfa_level = 'Enabled'
    else:
        mfa_level = 'Disabled'
    if default_notifactions == discord.NotificationLevel.only_mentions:
        default_notifactions = 'Only Mentions'
    else:
        default_notifactions = 'All Messages'
    server = discord.Embed(
        title=name,
        description=f"{emoji2}⦁ **Server Name:** {name}\n{emoji2}⦁ **Server Id:** {id}\n{emoji2}⦁ **Server Region:** {region}\n{emoji2}⦁ **Server Owner:** {owner}\n{emoji2}⦁ **Server Created At:** {created_at}\n\n{emoji3}⦁ **Member Count:** {member_count}\n{emoji3}⦁ **Number of Roles:** {len(roles)}\n{emoji3}⦁ **Number of Channels:** {len(channels)}\n\n{emoji}⦁ **Number of Boosters:** {len(boosters)}\n{emoji}⦁ **Number of Boosts:** {boostes}\n{emoji}⦁ **Boost Level:** {boost_level}\n\n{emoji4}⦁ **Default Notfactions:** {default_notifactions}\n{emoji4}⦁ **Explicit Content Filter:** {content_filter}\n{emoji4}⦁ **Verification Level:** {verification_level}\n{emoji4}⦁ **2 Factor Verfication:** {mfa_level}"
    )
    server.add_field(name=f"{emoji5}⦁ Server Features", value=features.lower(), inline=True)
    server.add_field(name=f"{emoji6}⦁ Invite Link", value=invite[0:25], inline=True)
    server.set_thumbnail(url=icon)
    await ctx.send(embed=server)


@client.command()
async def avatar(ctx, *, member: typing.Optional[discord.Member] = None):
    if member == None:
        member = ctx.author
    name = member.name
    avatar = discord.Embed(
        title=f"{name}'s Avatar"
    )
    avatar.set_image(url=member.avatar_url)
    await ctx.send(embed=avatar)


@client.command()
async def bug(ctx, *, bug: str):
    channel = client.get_channel(761438601418113094)
    bug = discord.Embed(
        title=f"Bug from {ctx.author}",
        description=f"**Bug Reporter:** {ctx.author}\n**Reporter Id:** {ctx.author.id}\n**From Server:** {ctx.guild.name}\n**Server Id:** {ctx.guild.id}\n\nBug Reported: \n{bug}"
    )
    await channel.send(embed=bug)
    await ctx.send("Bug Reported!")


@client.command()
async def info(ctx):
    owner = client.get_user(757003443779928196)
    name = client.user.name
    guild = client.guilds
    member_list = client.get_all_members()
    members = [member.id for member in member_list]
    info = discord.Embed(
        title=f"About {name}",
        colour=0x770505
    )
    info.add_field(name="Version", value='1.2.0', inline=True)
    info.add_field(name="Library", value='discord.py', inline=True)
    info.add_field(name="Creator", value=f"{owner.name} #{owner.discriminator}", inline=True)
    info.add_field(name="Servers", value=len(guild), inline=True)
    info.add_field(name="Users", value=len(members), inline=True)
    info.add_field(name="Support Server", value='https://discord.gg/H7hceVz', inline=True)
    info.set_footer(text=f"User {prefix}bug [reason] to report a bug.", icon_url=client.user.avatar_url)
    info.timestamp
    await ctx.send(embed=info)

@client.group()
async def ticket(ctx):
    guild = ctx.message.guild
    log = client.get_channel(759635212945981481)


@ticket.command()
async def new(ctx, *, reason=None):
    guild = ctx.message.guild
    guild_check = client.get_guild(758371378721587241)
    if guild == guild_check:
        role = discord.utils.get(guild.roles, id=760218656092454993)
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            guild.me: discord.PermissionOverwrite(read_messages=True),
            ctx.author: discord.PermissionOverwrite(send_messages=True, read_messages=True, manage_channels=True),
            role: discord.PermissionOverwrite(send_messages=True, read_messages=True, manage_channels=True)
        }
        channel = await guild.create_text_channel(f"ticket {ctx.author.discriminator}", overwrites=overwrites)
        await ctx.send(f"Ticket has been created. The ticket is <#{channel.id}>")
        await channel.send(f"<@{ctx.author.id}> <@&760218656092454993>")
        embed = discord.Embed(
            title=f"**Ticket {ctx.author.discriminator}**",
            description=f"Thank you for making a Ticket Support will be with you soon.\n\n**Ticket By:** {ctx.author}\n**Reason for Ticket:** {reason}"
        )
        await channel.send(embed=embed)
        log_embed = discord.Embed(
            title=f"**{ctx.author} has made a ticket.**",
            description=f"Reason: {reason}\nTicket Channel: <#{channel.id}>"
        )
        await log.send(embed=log_embed)
    else:
        return


@ticket.command()
@commands.has_permissions(manage_channels=True)
async def close(message, *, reason=None):
    guild = message.guild
    guild_check = client.get_guild(758371378721587241)
    if guild == guild_check:
        channel = client.get_channel(message.channel.id)
        log = client.get_channel(759635212945981481)
        await channel.delete(reason=reason)
        log_embed = discord.Embed(
            title=f"**{message.author} has closed a ticket.**",
            description=f"Reason: {reason}"
        )
        await log.send(embed=log_embed)
    else:
        return

@client.command()
async def help(ctx):
    emoji = client.get_emoji(762111439582134343)
    help = discord.Embed(
        title=f"Help & Commands {emoji} (Prefix: {prefix})",
        description=f"`profile` - Shows someone's profile. This shows their user ID, Avatar, Roles, and more.\n\n`ticket` - Opens a ticket. Do `{prefix}ticket [reason]` to include a reason.\n\n`info` - Get info on the bot and a link to support server.\n\n`server` - Get info on the current server or a server the bot is in. Use `{prefix}server [server_id]` for servers the bot is in.\n\n`help` - Shows this menu."
    )
    help.set_thumbnail(url=ctx.guild.icon_url)
    await ctx.send(embed=help)

client.run('')
