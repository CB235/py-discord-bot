import discord
from discord.ext import commands
import time
import random

intents = discord.Intents.all()
client = commands.Bot(command_prefix = ";", intents = intents)
#, intents = intents)


#####bot status##
@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.idle, activity=discord.Game(name=';help'))
    print('bot ready')
    startmessage = (f'Bot is up and running, ping is {client.latency * 1000}ms')
    print(startmessage)
    

############################################SETUP##########

welcomegoodbye_channel = 
logs_channel = 
warn_channel = ''
bot_ver = "1.0"
TOKEN = ''
contact = ""



    
    
########COMMANDS####################



##########BOT HELP#######
client.remove_command('help')
@client.command()
async def help(ctx):
    embed=discord.Embed(title="Here's some help!", description="Here are the commands:", color=0x27ff00)
    #embed.set_image(url="https://media.discordapp.net/attachments/783367383908614164/784861106342330408/unknown.png")
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/783367383908614164/784861106342330408/unknown.png")
    embed.add_field(name="ban", value="bans the user, e.g ;ban @user", inline=False)
    embed.add_field(name="kick", value="Kicks the user, e.g ;kick @user", inline=False)
    embed.add_field(name="warn", value="Warns the user, e.g ;warn @user", inline=False)

    embed.add_field(name="clear", value="Clears messages, by default ;clear deletes 1 message, you can delete a custom amount of messages by specifying the number after clear, e.g ;clear 7", inline=False)
    embed.add_field(name="ping", value="Utility to see bot hosting server ping", inline=False)
    embed.add_field(name="flipcoin", value="Fun command to flip a coin", inline=False)
    embed.add_field(name="nitro", value="Fun command to gift totally real nitro", inline=True)
    embed.add_field(name="idiot", value="Fun command to trick an idiot", inline=True)
    embed.add_field(name="dance", value="Fun command to post a dancing gif", inline=True)
    embed.add_field(name="sillysentence", value="Fun command to generate a silly sentence", inline=False)
    embed.add_field(name="duck", value="Fun command to post an image of a duck", inline=False)
    embed.add_field(name="add", value="Fun command to add 2 numbers together, usage ;add 1 2", inline=False)
    embed.add_field(name="botver", value="Shows bot version", inline=True)
    embed.set_footer(text="Any problems or suggestions? Contact penguin#8420")
    #await ctx.send ("https://media.discordapp.net/attachments/783367383908614164/784861106342330408/unknown.png")
    await ctx.send(embed=embed)
    
    
    

    

##FUN##

@client.command()
async def flipcoin(ctx):
    """Gives you heads or tails"""
    coinstate = random.randint(0,1)
    if coinstate == 0:
        embed=discord.Embed(title= "Heads!", description = "You flipped Heads", color=0xff2d00)
        embed.set_thumbnail(url = "https://media.discordapp.net/attachments/783367383908614164/784873591673192448/unknown.png")
        embed.set_footer(text=f"Any problems or suggestions? Contact {contact}")
        await ctx.send(embed=embed)
    else:
        embed=discord.Embed(title= "Tails!", description = "You flipped tails", color=0xff2d00)
        embed.set_thumbnail(url = "https://media.discordapp.net/attachments/783367383908614164/784873591673192448/unknown.png")

        embed.set_footer(text=f"Any problems or suggestions? Contact {contact}")
        await ctx.send(embed=embed)
        
        
        
        
        
@client.command()
async def add(ctx, arg1, arg2):
    embed=discord.Embed(title="The answer is...", color=0x27ff00)
    embed.set_thumbnail(url = "")
    int(arg1)
    int(arg2)
    answerint = arg1 + arg2
    int(answerint)
    embed.add_field(name= arg1 + arg2, value= f"{arg1} + {arg2} = {answerint}", inline=False)
    embed.set_footer(text=f"Any problems or suggestions? Contact {contact}, this command is purely a joke.")
    
    await ctx.send(embed=embed)
    
        
        
        
        
@client.command()
async def nitro(ctx, amount = 1):
    await ctx.channel.purge(limit=amount)
    await ctx.send("https://media.discordapp.net/attachments/783367383908614164/784875370859593768/xedy9ugkqo621.png")
    
@client.command()
async def idiot(ctx, amount = 1):

    await ctx.channel.purge(limit=amount)
    
    await ctx.send("https://media.discordapp.net/attachments/783367383908614164/784877115635925063/s08k98n1y3r21.png")
    
    
@client.command()
async def dance(ctx):
    await ctx.send("https://tenor.com/view/dancing-excited-dance-dance-move-smile-gif-16099354")
    
    



@client.command()
async def sillysentence(ctx):
    
    silly_noun1 = ["boy", "girl", "man", "woman", "dog", "cat", "wombat", "ape", "tapir", "fox", "orangutan", "seagull", "tiger", "mouse", "alligator"]
    silly_noun2 = ["baseball", "chocolate", "beer", "hat", "college", "book", "table", "cup", "laptop", "light", "scissors", "leaf", "key"]
    silly_verb1 = ["dropped", "ate", "licked", "climbed", "sat on", "stood on", "lost", "gripped", "questioned", "hugged", "covered"]
    silly_transport = ["cycled to", "walked to", "flew to", "jumped to", "hopped to", "rolled to", "hobbled to", "teleported to", "ran to", "crawled to", "drove to", "boated to"]
    silly_place = ["the cinema", "the grocery store", "the park", "the school", "the hospital", "the pub", "the palace", "the airport", "the city", "the farm", "the forest", "the marketplace", "the opticians", "the restaurant"]
    
    
    sentence = (f"The {random.choice(silly_noun1)} {random.choice(silly_verb1)} the {random.choice(silly_noun2)}, then {random.choice(silly_transport)} {random.choice(silly_place)}.")
    await ctx.send(sentence)
    
    
@client.command()
async def duck(ctx):
    urls = ["https://media.discordapp.net/attachments/783367383908614164/784885594370998272/GettyImages-1146102607-b3491a355af94171aa8ac7b0aeec0616.png", "https://media.discordapp.net/attachments/783367383908614164/784885645499301959/duckling-close-up-500315849-572917c93df78ced1f0b99ec.png?width=682&height=384", "https://media.discordapp.net/attachments/783367383908614164/784885658807173120/1200px-Grave_eend_maasmuur.png?width=416&height=384", "https://media.discordapp.net/attachments/783367383908614164/784885675203100682/GettyImages-134573694-4450067f8294477d8ea9a88c5017e1a1.png?width=384&height=384", "https://media.discordapp.net/attachments/783367383908614164/784885716048019456/iStock_000015316532_thierry-vialard-602x399.png?width=579&height=384", "https://media.discordapp.net/attachments/783367383908614164/784885752664293396/2427770107_e7be35d768_o-e1475851811724.png?width=682&height=384", "https://media.discordapp.net/attachments/783367383908614164/784885778559008768/2Q.png", "https://media.discordapp.net/attachments/783367383908614164/784885807311880252/235044.png?width=576&height=384" "https://media.discordapp.net/attachments/783367383908614164/784885941638135839/gettyimages-153946484-1-1575996437.png?width=577&height=384", "https://media.discordapp.net/attachments/783367383908614164/784885983312478208/5132.png?width=384&height=384", "https://media.discordapp.net/attachments/783367383908614164/784886054456393738/cole-keister-tpL5jONGQPY-unsplash-1.png?width=576&height=384", "https://media.discordapp.net/attachments/783367383908614164/784886077282451506/13597480_web1_180920-CVA-Ducks-Unlimited_1-1280x720.png?width=682&height=384", "https://media.discordapp.net/attachments/783367383908614164/784886099717259325/31977.png", "https://media.discordapp.net/attachments/783367383908614164/784886127869165588/a780d8f211dfdae66dacf9547e45fbbc.png?width=551&height=384", "https://media.discordapp.net/attachments/783367383908614164/784886175470321674/ducks-about-ducks-history-baby-duck-screenshot-2019-09-05-at-50033-pm_d5e702a1.png?width=501&height=384", "https://media.discordapp.net/attachments/783367383908614164/784886202599604244/images.png"]
    await ctx.send(random.choice(urls))
            
    
        
    


##echo##
@client.command()
async def echo(ctx, arg1, arg2):
    """I say what you say"""
    await ctx.send('{} {}'.format(arg1, arg2))
    
@client.command()
async def e(ctx):
    embed=discord.Embed(title="E", color=0x27ff00)
    await ctx.send(embed=embed)




##UTILS##

@client.command()
async def ping(ctx):
    """Utility to see server ping"""
    pingmessage = (f'ping is {client.latency * 1000}ms')
    embed=discord.Embed(title="Ping Utility", description= pingmessage, color=0x27ff00)
    embed.set_thumbnail(url = "https://media.discordapp.net/attachments/783367383908614164/784873660384673822/unknown.png")
    embed.add_field(name="ping", value="Utility to see bot hosting server ping", inline=False)
    embed.set_footer(text=f"Any problems or suggestions? Contact {contact}")
    await ctx.send(embed=embed)
    
    

@client.command()
async def botver(ctx):
    embed=discord.Embed(title="Bot version", description=f"Version: {bot_ver}", color=0x27ff00)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/783367383908614164/784861106342330408/unknown.png")

    
    await ctx.send(embed = embed)
    
    

        


##CLEAR MESSAGES##

@client.command()
@commands.has_permissions(ban_members = True)
@commands.has_permissions(kick_members = True)
async def clear(ctx, amount = 1):
    """clears messages"""
    await ctx.channel.purge(limit=amount)
    #await ctx.channel.purge(limit = 1)
    embed=discord.Embed(title="Messages cleared!", color=0x27ff00)
    embed.set_thumbnail(url="https://images-ext-2.discordapp.net/external/8w58jY4pZlGMJMEfaXD3QSHfso_FnScROBQUlWDrJIs/https/media.discordapp.net/attachments/783367383908614164/784871009076772864/unknown.png")
    embed.add_field(name="Tip:", value="Always be careful clearing messages, you never know what important info you may accidentally delete.", inline=False)
    embed.set_footer(text=f"Any problems or suggestions? Contact {contact}")
    await ctx.send(embed=embed)
    channel = client.get_channel(logs_channel)
    await channel.send("Messages cleared")
    
    
    
    
    
    
##KICK MEMBER##
@client.command()
@commands.has_permissions(kick_members = True)
async def kick(ctx, member : discord.Member, *, reason=None):
    #"""Kicks a member"""
    await member.kick(reason=reason)
    kickmessage = (f"User {member} has been kicked.")
    embed=discord.Embed(title="User succesfully kicked!", description = kickmessage, color=0x0082ff)
    embed.set_image(url = "https://media.discordapp.net/attachments/783367383908614164/784891362457813002/unknown.png")
    
    embed.set_footer(text=f"Any problems or suggestions? Contact {contact}")
    await ctx.send(embed=embed)
    channel = client.get_channel(logs_channel)
    await channel.send(kickmessage)


##BAN MEMBER#########
@client.command()
@commands.has_permissions(ban_members = True)
async def ban(ctx, member : discord.Member, *, reason=None):
    #"""Bans a member"""
    await member.ban(reason=reason)
    banmessage = (f"User {member} has been banned")
    
    embed=discord.Embed(title="User succesfully banned!", description = banmessage, color=0x0082ff)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/783367383908614164/784864469339734077/unknown.png")
    embed.add_field(name="To unban:", value="Go into settings>bans then select the user you want to unban, then press revoke ban.", inline=False)
    embed.set_footer(text=f"Any problems or suggestions? Contact {contact}")
    await ctx.send(embed=embed)
    channel = client.get_channel(logs_channel)
    await channel.send(f"{banmessage}, bot version{bot_ver}")


    

###WARN#####
@client.command()
async def warn(ctx, member):
    embed=discord.Embed(title= f"{member} has been warned.", description= f"If you want to appeal this decision, please feel free to contact {contact} ", color=0xff2d00)
    embed.set_image(url = "https://media.discordapp.net/attachments/783367383908614164/785216480550977546/unknown.png")
    embed.set_footer(text=f"Any problems or suggestions? Contact {contact}")
    await ctx.send(embed = embed)
    channel = client.get_channel(logs_channel)

    await channel.send(embed = embed)
    

     
    
    
    
#NEW MEMBER##
@client.event
async def on_member_join(member):
    print(f'{member} has joined the server.')
    channel = client.get_channel(welcomegoodbye_channel)
    welcomemessage_title = (f'{member} has joined the server!')
    welcomemessage_description = (f"Welcome to the server, {member}!")
    embed=discord.Embed(title= welcomemessage_title, description= welcomemessage_description, color=0xff2d00)
    embed.set_footer(text=f"Any problems or suggestions? Contact {contact}")
    await channel.send(embed = embed)
    #print("new member")
    channel = client.get_channel(logs_channel)
    await channel.send(f"{member} has joined the server")
    


    

    
    
#LEAVE MEMBER#
@client.event
async def on_member_remove(member):
    print(f'{member} has left server')
    channel = client.get_channel(welcomegoodbye_channel)
    await channel.send(f'{member} has left the server :c')
    goodbyemessage_title = (f'{member} has left the server!')
    goodbyemessage_description = (f"Farewell, {member}!")
    embed=discord.Embed(title= goodbyemessage_title, description= goodbyemessage_description, color=0xff2d00)
    embed.set_footer(text=f"Any problems or suggestions? Contact {contact}")
    await channel.send(embed = embed)
    channel = client.get_channel(logs_channel)
    await channel.send(f"{member} has left the server")
    


    
    




client.run(TOKEN)
