import discord, json
from discord.ext import commands
from discord_components import DiscordComponents, Button, ButtonStyle

with open('./config/config.json', 'r') as sy:
    system = json.load(sy)

client = commands.Bot(command_prefix = system['prefix'], intents = discord.Intents.all())
DiscordComponents(client)

@client.event
async def on_ready():
    print(f'Bot Name: {client.user} / Bot Id: {client.user.id}')
    print(f'Bot participating servers: {client.guilds}')
    print('Bot Online / Dev. BestHentai0 / https://github.com/BestHentai0')

@client.command(name='notice')
async def Notice(ctx, *, arg):
    if not ctx.author.guild_permissions.administrator:
        return await ctx.send(f'{ctx.author.mention}, You are not a manager.')
    channel = client.get_channel(system['notiy_channel'])
    embed = discord.Embed(color=0xab19ae, timestamp=ctx.message.created_at, title="Notice", description="_```md\n# Server Notice```_")
    embed.set_image(url="https://cdn.discordapp.com/attachments/962151732614410290/975338541896851466/Ys__0.png?size=4096")
    embed.add_field(name="――――――――――――――――――――――――――――", value=arg, inline=True)
    embed.set_footer(text=f'Admin: {ctx.author}')
    await channel.send("@everyone", embed=embed)
    await ctx.send('Finished appointment')
    await ctx.message.delete()

client.run(system['token'])