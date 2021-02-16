        # Imports (eu recomendava instalares todos menos o "random", só se precisares)
import os
import discord
import asyncio
from discord import member
from discord.ext import commands
import random
from discord.ext.commands.core import command

        # Escolher prefixo do bot
client = commands.Bot(command_prefix=['bot '])

        # Esta parte acho que é essencial para qualquer bot (serve para te dizer quando o bot já ligou)
@client.event
async def on_ready():
    print('Prontinho!')
        # Esta parte é opcional, mas serve para mudares o status do bot
@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('Tic Tac Toe'))
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))


op8ball=['Parece-me que sim',' Agora estou a passar a ferro.',''
    ' Ainda não tens idade para saber isso.','Vou ver se está a chover lá fora',
    'Pergunta à tua prima','Não contava com isso.','Está mais que óbvio.',
    'Sim, acho que vi isso no youtube','É provável.','Not gonna happen, darling','A tua mãe disse me que não.','Não vejo as coisas a encaminharem-se bem... ||<:kekw:763874819883925505>||',
    'Deus está connosco 🙏','Vai mas é rezar um credo.','Acredito mesmo que sim','Dúvido, queridx...','Sem dúvida!','Sim!','Sim, definitivamente ','Só Deus sabe...']

        #  MEME

@client.event
async def on_message(msg):
    kek: str = msg.content
    x=kek.lower()
    if 'b responde ' in x or 'b adivinha ' in x or 'b 8ball' in x or 'b diz ' in x:
        await msg.reply(f'{random.choice(op8ball)}')
    if 'cisco' in x:
        await msg.add_reaction('<:ciscoapoggar:809032623354544178>')
    if 'aoco' in x or 'mdis' in x or 'torcato' in x:
        await msg.add_reaction('<:ELIMINAR:767703787712282635>')
    if 'aoco' in x:
        await msg.add_reaction('<:weirdcanas:810630123975868426>')
    if 'amen' in x or 'finalmente' in x or 'politica' in x or 'política' in x:
        await msg.add_reaction('<:zearezar:809032623480504342>')
    if 'peras' in x:
        await msg.add_reaction('<:perasarezar:809032623825485824>')
        await msg.add_reaction('<:omaria:809032624168763432>')
        await msg.add_reaction('<:JAVAGAY:799242001173577728>')
    if 'luisinha' in x:
        await msg.add_reaction('<:kuisapoggers:809032623758114876>')
    if 'mano' in x:
        await msg.add_reaction('<:mano:809032623644082206>')
    if 'pog' in x or 'lezgo' in x or 'lfg' in x or 'lets go' in x:
        await msg.add_reaction('<:poggies:789853745855856660>')
    if 'lima' in x or 'peras' in x or 'gui' in x:
        await msg.add_reaction('<:ehehe:761324245308932127>')
    if 'sporting' in x:
        await msg.add_reaction('<:homemsporting:790192696294637578>')
    if 'ubuntu' in x or 'bash' in x or 'linux' in x or 'sex' in x or 'arch' in x:
        await msg.add_reaction('🇸')
        await msg.add_reaction('🇪')
        await msg.add_reaction('🇽')
        await msg.add_reaction('🇴')
        await msg.add_reaction('💦')
        await msg.add_reaction('👅')
    if 'quero falecer' in x or'suicidio' in x or 'suicídio' in x or 'me matar' in x or 'atirar-me' in x or 'atirar me' in x or 'me atirar' in x or'mandar-me' in x or 'mandar me' in x or 'me mandar' in x or 'quero morrer' in x:
        await msg.reply('''> :telephone: **SOS ESTUDANTE**  ``96 955 45 45 ou 808 200 204 (20h à 1h)`` \n > http://www.adcl.org.pt/observatorio/servicos.php?titulo=Linhas''')
    if 'dormir' in x or 'sono' in x or 'sleep' in x:
        await msg.add_reaction('<:residentsleeper:768410966123479043>')
    if 'covid' in x or 'couve' in x or 'corona' in x:
        await msg.add_reaction('😷')

# AULAS
    if 'aulas mieic' in x or 'aulas info' in x:
        await msg.reply('''>                                                     ```fix
    > --"MEST"--
    > ``` <https://site.com>
    >
    > ```css
    > --"PROG"--
    > ```
    >
    > ```bash
    > --"FIS1"--
    > ```
    >
    > ```ini
    > [--CMAT--]
    > ```
    >
    > ```diff
    > --MPCP--
    > ```
    ''')
    if 'poll:' in x:
        await msg.add_reaction('👍')
        await msg.add_reaction('👎')
    await client.process_commands(msg)

'''MENSAGEM DE ERRO'''

err=['Só posso estar a ouvir mal...','Esse comando não existe!', 'Não digas asneiras!', 'Estou surda...', 'Não consigo entender.',
     'Tenho de trocar as pilhas do minissom...', 'Agora é que ia bem uma francesinha...']
@client.event
async def on_command_error(ctx, error):
    print("ERROR", error, type(error))
    if isinstance(error, commands.errors.CommandNotFound):
        await ctx.reply(f'{random.choice(err)}')


token=os.getenv('TOKEN', '')
client.run(token)