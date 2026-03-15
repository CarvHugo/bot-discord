import discord
from discord.ext import commands
from random import randint
import asyncio

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def sus(ctx):
    await ctx.send('**AMOGUS**')
    
@bot.command()
async def dado(ctx):
    await ctx.send(f':game_die: {randint(1,6)} no dado!')

audios = {
"tung": "https://www.myinstants.com/media/sounds/tung-tung-tung-tung-tung-tung-sahur.mp3",
"recuperamos": "https://www.myinstants.com/media/sounds/recuperamos-a-bola.mp3",
"wombo": "https://www.myinstants.com/media/sounds/wombo-combo.mp3",
"skibidi": "https://www.myinstants.com/media/sounds/skibidi-toilet.mp3",
"aura" : "https://www.myinstants.com/media/sounds/auraa.mp3",
"tralalelo" : "https://www.myinstants.com/media/sounds/tralalelo-tralala_xfWZjq1.mp3",
"skyrim" : "https://www.myinstants.com/media/sounds/skeleton-with-shield.mp3",
"baad" : "https://www.myinstants.com/media/sounds/bad-to-the-bone-meme.mp3",
"boom" : "https://www.myinstants.com/media/sounds/vineboom-long.mp3",
"bruh" : "https://www.myinstants.com/media/sounds/bruh-sound-effect-1.mp3",
"oof" : "https://www.myinstants.com/media/sounds/roblox-death-sound_1.mp3",
"oof2" : "https://www.myinstants.com/media/sounds/roblox-death-sound_ytkbl7x.mp3",
"buzina" : "https://www.myinstants.com/media/sounds/rap-intro-outro-air-horn-sound.mp3",
"mygod" : "https://www.myinstants.com/media/sounds/video0-11.mp3"
}
    
@bot.command()
async def memes(ctx):
    lista = "\n".join(audios.keys())

    mensagem = f"""**Lista de Memes**

{lista}

**Lembrete**: digite !play (nome do meme) para executar o áudio.
"""

    await ctx.send(mensagem)
    
@bot.command()
async def play(ctx, audio):

    if audio not in audios:
        await ctx.send("Esse meme não consta no database do bot.")
        return
    
    elif ctx.author.voice is None: # Se o usuário estiver fora do canal de voz
        await ctx.send("Entre em um canal de voz primeiro!")
        return
    
    canal = ctx.author.voice.channel
    voice = ctx.voice_client
    
    if voice is None: # Se o bot estiver fora do canal de voz
        voice = await canal.connect() # Conecta ao canal de voz quando requisitado
        
    elif voice.channel != canal: # Se o canal de voz do usuário for diferente do canal do bot
        await voice.move_to(canal) # Bot se desloca ao canal do usuário
        
    escolha = audios[audio] # fatia o áudio escolhido no dicionário audios
    
    await asyncio.sleep(0.3) # Pequena espera para reproduzir o áudio e assim evitar bugs
    voice.play(discord.FFmpegPCMAudio(escolha))
    
    while voice.is_playing():
        await asyncio.sleep(0.5) # Pequena espera para evitar que o áudio seja cortado no final
    await voice.disconnect()
    
@bot.command()
async def stop(ctx):

    voice = ctx.voice_client

    if voice is None: #Se o bot não estiver em um canal de voz
        await ctx.send("Não estou em um canal de voz.")
        return

    if voice.is_playing(): # Se o bot está reproduzindo algum meme
        voice.stop() # Interrompe a reprodução
        await ctx.send("Áudio encerrado. :-]")
        
@bot.command()
async def info(ctx):
    informacoes = """**Botinho**

Um bot de memes!

Criado por Hugo Carvalho

Entre em contato em caso de bugs, sugestões ou elogios:
hugoncarv@gmail.com
"""

    await ctx.send(informacoes)

@bot.command()
async def comandos(ctx):
    comandos = """
    **Lista de comandos**

!comandos :right_arrow: Exibe todos os comandos do bot
!info :right_arrow: Exibe informações sobre o bot
!sus :right_arrow: Bot responde **AMOGUS**
!dado :right_arrow: Bot rola um dado de 6 lados
!memes :right_arrow: Exibe a lista de memes do bot
!play (nome do meme) :right_arrow: Reproduz o meme escolhido no seu canal de voz
!stop :right_arrow: Interrompe a reprodução do meme
    """
    await ctx.send(comandos)

bot.run('Seu Token aqui')