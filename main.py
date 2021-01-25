import keep_alive
import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix = '/')
client.remove_command("help")

winlose = ['w/l', 'W/l', 'w/L', 'W/L']

@client.group(invoke_without_command=True)
async def help(ctx):
    em = discord.Embed(title="Commands!" , color = 6862847)

    em.add_field(name = "**Moderation** \n <> mandatory arguments [] optional arguments \n type ?help (command) for more information on a command!", value = " - kick \n- ban \n- unban \n- mute \n- unmute \n- purge \n- warn \n- slowmode \n**Misc** \n- ping \n-userinfo \n-credits")

    await ctx.send(embed = em)

@help.command()
async def mute(ctx):
    em = discord.Embed(title ="Description:", description = "Mutes a member so they cannot send messages.", color = 00000000)

    em.add_field(name = "Example:", value = "?mute <member> [reason]", inline = True)

    await ctx.send(embed = em)

@help.command()
async def unmute(ctx):
    em = discord.Embed(title ="Description:", description = "Unmutes a member and allows them to speak again.", color = 00000000)

    em.add_field(name = "Example:", value = "?unmute <member>", inline = True)

    await ctx.send(embed = em)

@help.command()
async def ban(ctx):
    em = discord.Embed(title ="Description:", description = "Bans a member from the guild/server.", color = 00000000)

    em.add_field(name = "Example:", value = "?ban <member> [reason]", inline = True)

    await ctx.send(embed = em)

@help.command()
async def purge(ctx):
    em = discord.Embed(title ="Description:", description = "Clears messages.", color = 00000000)

    em.add_field(name = "Example:", value = "?purge <# of messages>", inline = True)

    await ctx.send(embed = em)

@help.command()
async def warn(ctx):
    em = discord.Embed(title ="Description:", description = "Warns a member.", color = 00000000)

    em.add_field(name = "Example:", value = "?warn <member> [reason]", inline = True)

    await ctx.send(embed = em)

@help.command()
async def slowmode(ctx):
    em = discord.Embed(title ="Description:", description = "Adds slowmode to a channel. (sorry for the inconvenience, but you can only go by seconds.)", color = 00000000)

    em.add_field(name = "Example:", value = "?slowmode <time>", inline = True)

    await ctx.send(embed = em)

@help.command()
async def kick(ctx):
    em = discord.Embed(title ="Description:", description = "Kicks a member from the guild/server.", color = 00000000)

    em.add_field(name = "Example:", value = "?kick <member> [reason]", inline = True)

    await ctx.send(embed = em)

@help.command()
async def unban(ctx):
    em = discord.Embed(title ="Description:", description = "Unbans a member from the guild/server.", color = 00000000)

    em.add_field(name = "Example:", value = "?unban <User#Tag>", inline = True)

    await ctx.send(embed = em)

@client.event
async def on_ready():
   await client.change_presence(activity=discord.Activity(type = discord.ActivityType.listening, name = "a student council meeting"))

@client.command()
async def ping(ctx,):  
    await ctx.send('Pong!')

@client.command()
async def credits(ctx,):

    emb = discord.Embed(title = "Credits!", color = 00000000)

    emb.add_field(name = "main developer:", value = "angelmallow#3087")
    emb.add_field(name = "testers:", value = "Gp#3087 \n୨୧・₊˚ hxneybee・#0001 \n𝙼𝚒𝚗𝚒 シ#5986")
    emb.add_field(name = "inspiration:", value = "Yumemi#3553 (also my bot)")
    emb.add_field(name = "dev notes:", value = "Thanks so much to all the testers that let me test commands on them! Without them, I probably would still have a broken mute command... love you three!")

    await ctx.send(embed = emb)

@client.command(aliases=['m'])
@commands.has_permissions(kick_members=True)
async def mute(ctx,member : discord.Member,*,reason = "No reason has been provided."):
   muted_role = ctx.guild.get_role(733781532988407861)

   await member.add_roles(muted_role)

   await member.send(member.mention + " has been muted. Reason: "+reason)

   await ctx.send(member.mention + " has been muted. Reason: "+reason)

@client.command()
@commands.has_permissions(manage_channels=True)
async def slowmode(ctx, seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(f"I set the slowmode in this channel to {seconds} seconds!")

@client.command(aliases=['p','c'])
@commands.has_permissions(kick_members=True)
async def clear(ctx, amount=2):
	await ctx.channel.purge(limit=amount)

@client.command(aliases=['k'])
@commands.has_permissions(kick_members = True)
async def kick(ctx,member : discord.Member,*,reason = "No reason has been provided."):

    await member.send(member.name + " has been kicked from the server. Reason: "+reason)

    await ctx.send(member.name + " has been kicked from the server. Reason: "+reason)

    await member.kick(reason = reason)

@client.command(aliases=['b'])
@commands.has_permissions(ban_members = True)
async def ban(ctx,member : discord.Member,*,reason = "No reason has been provided."):
    await member.send(member.name + " has been banned from the server. Reason: "+reason)

    await ctx.send(member.name + " has been banned from the server. Reason: "+reason)
      
    await member.ban(reason = reason)

@client.command(aliases=['ub'])
@commands.has_permissions(ban_members=True)
async def unban(ctx,*,member):
    banned_users = await ctx.guild.bans()
    member_name, member_disc, = member.split('#')

    for banned_entry in banned_users:
            user = banned_entry.user

            if(user.name, user.discriminator)==(member_name,member_disc):

                await ctx.guild.unban(user)
                await ctx.send(member_name +" has been unbanned!")
                return
    
@client.command(aliases=['um'])
@commands.has_permissions(kick_members=True)
async def unmute(ctx,member : discord.Member):
    muted_role = ctx.guild.get_role(733781532988407861)

    await member.remove_roles(muted_role)
    
    await ctx.send(member.mention + " has been unmuted!")
    
@client.command(aliases=['w'])
@commands.has_permissions(kick_members=True)
async def warn(ctx,member : discord.Member,*,reason= "no reason provided"):
      await member.send(member.name + " has been warned, **reason:** "+reason)
      
      await ctx.send(member.name + " has been warned, **reason:** "+reason)
      await member.warn(reason=reason)

@client.command()
async def userinfo(ctx, member: discord.Member):
	embed = discord.Embed(
	    title="**User Info**" , description=member.mention + "**'s profile has loaded successfully.**" , color=00000000)
	embed.add_field(name="ID!", value=member.id, inline=True)
	embed.add_field(name="Join Date!", value=member.joined_at.strftime("%a, %#d %b %Y, %I:%M %p CST"), inline=True)
	embed.add_field(
	    name="Account Creation!", value=member.created_at.strftime("%a, %#d %b %Y, %I:%M %p CST"), inline=True)
	embed.add_field(
	    name="Top Role!", value=member.top_role.mention, inline=True)
	embed.set_thumbnail(url=member.avatar_url)
	embed.set_footer(
	    icon_url=ctx.author.avatar_url, text=f"requested by {ctx.author.name}")
	await ctx.send(embed=embed)

@client.event
async def on_command_error(ctx,error):
	if isinstance(error,commands.MissingPermissions):
		await ctx.send("You don't have permissions to do that, " + ctx.author.mention + "!")
	if isinstance(error,commands.MissingRequiredArgument):
		await ctx.send("I'm sorry, you may have... forgotten to add something to the command. Please try again.")

	else:
		traceback.print_exception(type(error), error, error.__traceback__)

@client.event
async def on_message(msg):
	if msg.author == client.user:
		return None

	for word in winlose:
		if word in msg.content:
 			await msg.add_reaction ("<:p_cherryblossoms:787504360686092299>")
	await client.process_commands(msg)

keep_alive.keep_alive()
token = os.environ.get("Token")
client.run(token)
