import os
import discord
import asyncio
from discord import member
from discord.ext import commands
import random
from discord.ext.commands.core import command

client = commands.Bot(command_prefix=['bot '])


@client.event
async def on_ready():
    print('Prontinho!')


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game('Tic Tac Toe'))
    print('Connected to bot: {}'.format(client.user.name))
    print('Bot ID: {}'.format(client.user.id))


op8ball = ['Parece-me que sim', ' Agora estou a passar a ferro.', 'Ainda não tens idade para saber isso.',
           'Vou ver se está a chover lá fora',
           'Pergunta à tua prima', 'Não contava com isso.', 'Está mais que óbvio.',
           'Sim, acho que vi isso no youtube', 'É provável.', 'Not gonna happen, darling',
           'A tua mãe disse me que não.', 'Não vejo as coisas a encaminharem-se bem... ||<:kekw:763874819883925505>||',
           'Deus está connosco 🙏', 'Vai mas é rezar um credo.', 'Acredito mesmo que sim', 'Dúvido, queridx...',
           'Sem dúvida!', 'Sim!', 'Sim, definitivamente ', 'Só Deus sabe...']

erro = ['Só posso estar a ouvir mal...', 'Esse comando não existe!', 'Não digas asneiras!', 'Estou surda...',
        'Não consigo entender.',
        'Tenho de trocar as pilhas do minissom...', 'Agora é que ia bem uma francesinha...']


@client.event
async def on_command_error(ctx, error):
    print("ERROR", error, type(error))
    if isinstance(error, commands.errors.CommandNotFound):
        await ctx.reply(f'{random.choice(erro)}')


@client.event
async def on_message(msg):
    m: str = msg.content
    x = m.lower()
    if 'poll:' in x:
        await msg.add_reaction('👍')
        await msg.add_reaction('👎')
    if 'comunicado:' in x:
        await msg.add_reaction('✅')
    else:
        # -----------------------------EMOJIS USERS-----------------------------------------------
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
        if 'sex' in x:
            await msg.add_reaction('🇸')
            await msg.add_reaction('🇪')
            await msg.add_reaction('🇽')
            await msg.add_reaction('🇴')
            await msg.add_reaction('💦')
            await msg.add_reaction('👅')
        if 'ubuntu' in x or 'bash' in x or 'arch' in x or 'linux' in x or 'mint' in x:
            await msg.add_reaction('🤓')
        if 'ramalho' in x:
            await msg.add_reaction('<:OLA:811367924161839174>')
        if 'grr' in x:
            await msg.add_reaction('<:madiana:809032623379972127>')
        if 'frog' in x or '317653551939846144' in x:
            await msg.add_reaction('🐸')
        if 'balta' in x or '<@!100288993039499264>' in x:
            await msg.add_reaction('<:balta:811345262151860265>')
        # -------------------------FUNNY--------------------------------------
        if 'pfv responde ' in x or 'pfv adivinha ' in x or 'pfv 8ball' in x or 'pfv diz ' in x:
            await msg.reply(f'{random.choice(op8ball)}')
        if 'quero falecer' in x or 'suicidio' in x or 'suicídio' in x or 'me matar' in x or 'atirar-me' in x or 'atirar me' in x or 'me atirar' in x or 'mandar-me' in x or 'mandar me' in x or 'me mandar' in x or 'quero morrer' in x:
            await msg.reply(
                '''> :telephone: **SOS ESTUDANTE**  ``96 955 45 45 ou 808 200 204 (20h à 1h)`` \n > http://www.adcl.org.pt/observatorio/servicos.php?titulo=Linhas''')
        if 'dormir' in x or 'sono' in x or 'sleep' in x:
            await msg.add_reaction('<:residentsleeper:768410966123479043>')
        if 'covid' in x or 'couve' in x or 'corona' in x:
            await msg.add_reaction('😷')
        if 'mata-te' in x or 'mata te' in x:
            await msg.delete()
            await msg.channel.send('<:ban:798887475254657074>')
        # --------------------------ÚTIL--------------------------------------
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
    # ----------BEBIDAS---------BEBIDAS------------BEBIDAS---------BEBIDAS-----------BEBIDAS----------BEBIDAS--------------
    if 'pfv cafe' in x or 'pfv café' in x:
        await msg.reply('Cafézinho? Dá-me 5 segundos!')
        await msg.channel.send('https://cdn.dribbble.com/users/1172503/screenshots/4477752/coffee.gif')
        await asyncio.sleep(5)
        await msg.reply(f'Aqui está, feupinhx')
        await msg.channel.send(
            'https://upload.wikimedia.org/wikipedia/commons/thumb/a/ad/Cup-o-cofee-no-spoon.svg/1200px-Cup-o-cofee-no-spoon.svg.png')
    if 'pfv espresso' in x or 'pfv expresso' in x:
        await msg.reply('Estás preso????!')
        await asyncio.sleep(1)
        await msg.channel.reply('AHHHH EXPRESSO!!!! \nA sair!')
        await msg.channel.send('https://i.pinimg.com/originals/fb/f6/b2/fbf6b2c2ea3419bf28e5d45431228897.gif')
        await asyncio.sleep(5)
        await msg.reply('Aqui está! \nhttps://media-cdn.tripadvisor.com/media/photo-s/0d/12/a5/3b/cafe-expresso.jpg')
    if 'pfv cappuccino' in x or 'pfv capuccino' in x:
        await msg.reply('Aqui está, feupinhx. Conheces a história do capuchinho vermelho?')
        await msg.channel.reply('https://pngimg.com/uploads/cappuccino/cappuccino_PNG73.png')
    if 'pfv chocolate quente' in x:
        await msg.channel.send('Chocolatinho quentinho! O meu preferido!')
        await msg.reply(
            'https://s2.glbimg.com/Z9xyXL6yq6047CxOjzEHyGFchVo=/1200x/smart/filters:cover():strip_icc()/i.s3.glbimg.com/v1/AUTH_e84042ef78cb4708aeebdf1c68c6cbd6/internal_photos/bs/2020/Y/C/HMEPrvTga7o8TsGIhlOw/chocolate-quente.jpg')
    if 'pfv chá de ervas' in x or 'pfv cha de ervas' in x:
        await msg.reply('Cházinho de ervas a sair!')
        await msg.channel.send(
            'https://www.freepnglogos.com/uploads/tea-png/tea-top-afternoon-teas-around-the-red-letter-days-blog-8.png')
    if 'pfv chá de limonete' in x or 'pfv cha de limonete' in x:
        await msg.reply('Chá de limonete bem bom')
        await msg.channel.send(
            'https://conteudo.imguol.com.br/c/entretenimento/02/2017/08/03/cha-verde-1501773798026_v2_1920x1280.jpg')
    if 'pfv leit' in x:
        await msg.reply('Toma, feupinhx')
        await msg.channel.send(
            'https://cdn.shopify.com/s/files/1/2434/0841/products/dandelion-chocolate-pastry-milk-cookies-16449551597708_300x.jpg?v=1592956486')

    await client.process_commands(msg)


@client.command()
async def avatar(ctx, *, avamember: discord.Member = None):
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)


@client.command()
async def joined(ctx, *, member: discord.Member):
    await ctx.send('<@{0.id}> veio ser feupinho na data: ``{0.joined_at}``'.format(member, member))


@client.command()
async def ping(ctx):
    await ctx.send('pong xd: ``{0}s``'.format(round(client.latency, 1)))

token=os.getenv('TOKEN', '')
client.run(token)