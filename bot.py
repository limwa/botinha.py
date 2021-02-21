import os
import discord
import asyncio
from discord import member
from discord.ext import commands
import random
from discord.ext.commands.core import command
from discord.ext import commands


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
        if 'lima' in x or 'peras' in x or 'gui ' in x:
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
        if 'norberto' in x or 'costa freitas' in x or '<@!190968369791369216>' in x:
            await msg.add_reaction('🇵🇹')
            await msg.add_reaction('🧡')
        # -------------------------FUNNY--------------------------------------
        if 'pfv responde ' in x or 'pfv adivinha ' in x or 'pfv 8ball' in x or 'pfv diz ' in x:
            await msg.reply(f'{random.choice(op8ball)}')
        if 'quero falecer' in x or 'suicid' in x or 'me matar' in x or 'atirar-me' in x or 'atirar me' in x or 'me atirar' in x or 'mandar-me' in x or 'mandar me' in x or 'me mandar' in x or 'quero morrer' in x:
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
            embed = discord.Embed()
            embed.title = 'Aulas 1ºAno MIEIC'
            embed.color = 0x00a0a0
            embed.description = '''[CMAT](https://videoconf-colibri.zoom.us/j/87558364347?pwd=MStyUVpPSlEycmZvbWcrNGF0NnJxZz09) \n(seg 9:00-10:00 | qua 10:00-11:00)
            [FIS1](https://videoconf-colibri.zoom.us/j/82373725282?pwd=S1VrNEp4VkZYR2o1TUlPUW1hLzVhZz09)      \n(seg 10:00-11:00 | qua 9:00-10:00)
            [PROG](https://teams.microsoft.com/l/meetup-join/19%3a0a486ea7628247de956d27755601308e%40thread.tacv2/1613845204726?context=%7b%22Tid%22%3a%22b7821bc8-67cc-447b-b579-82f7854174fc%22%2c%22Oid%22%3a%22775956a4-e725-4eef-9eb9-da5057c8a6a6%22%7d) \n(seg 11:00-12:30 | qui 9:00-10:30)
            '''

            await msg.reply(embed=embed)
    # ----------BEBIDAS---------BEBIDAS------------BEBIDAS---------BEBIDAS-----------BEBIDAS----------BEBIDAS--------------
    if 'pfv menu' in x:
        await msg.reply('Cá está')
        await msg.channel.send('https://scontent.fopo2-1.fna.fbcdn.net/v/t1.0-0/p526x296/151939569_776368209936853_2010088215326660210_n.jpg?_nc_cat=103&ccb=3&_nc_sid=730e14&_nc_ohc=vvX4OXwKczcAX_A49PY&_nc_ht=scontent.fopo2-1.fna&tp=6&oh=bd32d7d10158aaa680d3a841d72893cd&oe=6051DEB1')
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
    if 'pfv moccachino' in x:
        await msg.reply('Here it is, feupinhx')
        await msg.channel.reply('https://media.istockphoto.com/photos/moccachino-coffee-on-table-top-picture-id502758012?k=6&m=502758012&s=612x612&w=0&h=AsBkeKFSY6PfdbRWfQ8NQqJZUhZ9eRkq6rX1kzlHr7U=p')
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
        await msg.channel.send('https://cdn.shopify.com/s/files/1/2434/0841/products/dandelion-chocolate-pastry-milk-cookies-16449551597708_300x.jpg?v=1592956486')
#-----especial
    emoji_miminho=['<a:hug:812076950155558912>','<a:beijinho:812078357361066024>', '<a:rena_gorda:812079912960786492>']
    if 'noodle' in x:
        await msg.channel.send('<a:ezgif:812000224217661491>')
    if 'miminho' in x:
        await msg.channel.send(f'{random.choice(emoji_miminho)}')
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
    await ctx.send('pong xd: ``{0}s``'.format(round(client.latency, 3)))

token=os.getenv('TOKEN', '')
client.run(token)