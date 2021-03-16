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
    m: str = msg.content.lower()
    '''if msg.guild.get_role(815327091163267092) in msg.author.roles:
        await msg.delete()'''
    if m.startswith('poll:'):
        if '|' not in m:
            await msg.add_reaction('👍')
            await msg.add_reaction('👎')
        else:
            poll_count = 1
            poll_react = {1: '🇦', 2: '🇧', 3: '🇨', 4: '🇩', 5: '🇪', 6: '🇫', 7: '🇬', 8: '🇭', 9: '🇮', 10: '🇯'}
            for poll_sep in m:
                if poll_sep == '|':
                    poll_count = poll_count + 1
            for poll_v in range(1, poll_count + 1):
                await msg.add_reaction(poll_react[poll_v])
    elif m.startswith('comunicado:'):
        await msg.add_reaction('✅')
    elif m.startswith('pfv 8ball'):
        embed = discord.Embed()
        embed.title = '✨🔮 Bola de Cristal 🔮✨'
        embed.color = 0x50327c
        img = ['https://www.lcmb.co.uk/wp-content/uploads/Crystal-ball.png',
               'https://images-na.ssl-images-amazon.com/images/I/617uBdvFrmL._AC_SX425_.jpg',
               'https://ak.picdn.net/shutterstock/videos/7716544/thumb/1.jpg',
               'https://mir-s3-cdn-cf.behance.net/project_modules/max_1200/3ae5f272857309.5bf5a63d4a181.png']
        embed.set_image(url=random.choice(img))
        embed.description = '💬 **Pergunta**: {0}\n\n🧙 O **grande mestre Botinho** diz: **{1}**'.format(m[9:],
                                                                                                         random.choice(
                                                                                                             op8ball))
        await msg.channel.send('https://i.gifer.com/YVPG.gif', delete_after=3.0)
        await asyncio.sleep(3)
        await msg.channel.send(embed=embed)
    elif m.startswith('pfv ajuda') or m.startswith('pfv help'):
        embed_help = discord.Embed()
        embed_help.color = (0x00FA9A)
        embed_help.title = ('🙋 Ajuda 🙋')
        embed_help.description = ('''Com que então pediste ajuda! Cá estou eu para te ajudar! 🔮

        **-----------------PREFIXO PFV-----------------**

***pfv 8bal [pergunta] →*** perdidx da vida? Mestre Botinho diz-te
***pfv waifu →*** owo
***pfv penis →*** mede-te a genitália (acho)
***pfv link** →*** dá-te um link para mandares invite aos teus amigos
***pfv mock [frasE paRA DaR MOCk] → ***dá mock


**-----------------PREFIXO BOT-----------------**

***bot avatar @user ->*** mostra o avatar da pessoa em grande
***bot joined @user →*** diz a data na qual o user se juntou ao server
***bot ping →*** um bocado inútil
***bot membros → ***retorna o número de membros do server (para melhorar)
***bot dm @user [mensagem]→*** manda uma mensagem privada com uma imagem fofinha


**-----------------EASTER EGGS 🐣----------------- **

miminho
noodle
trabalho de mest
aulas mieic/aulas info
... e bastantes reações

*INFO → o calado neste momento está desativado*

**Gostaste? 🤩 Considera dar-me uma estrelinha:**
https://github.com/golangis/botinha.py
        ''')
        channel = await msg.author.create_dm()
        await channel.send(embed=embed_help)

    elif m.startswith('pfv waifu'):
        embed = discord.Embed()
        embed.title = 'Waifu Meter'
        n = random.randint(0, 101)
        if n < 25:
            y = '🤢'
            embed.color = 0xff0000
        elif n < 50:
            y = '😳'
            embed.color = 0xffa500
        elif n < 75:
            y = '☺'
            embed.color = 0x0000ff
        else:
            y = '😻'
            embed.color = 0xffc0cb
        embed.description = 'És {0}% waifu. {1}'.format(n, y)
        await msg.reply(embed=embed)
    elif m.startswith('pfv pilau') or m.startswith('pfv penis') or m.startswith('pfv pénis'):
        embed = discord.Embed()
        embed.title = 'Penis Meter'
        b = random.randint(0, 40)
        embed.color = 0xffc0cb
        d = "8" + "-" * b + "D"
        embed.description = d
        await msg.reply(embed=embed)
    elif m.startswith('pfv link') or m.startswith('pfv invite'):
        await msg.reply('https://discord.gg/bQp7H5vpcX')
    elif m.startswith('pfv mock '):
        m = list(m)
        final_mock = ''
        for letter_mock in m[8:]:
            choices_mock = [letter_mock.lower(), letter_mock.upper()]
            if letter_mock.isalpha():
                v_mock = random.choice(choices_mock)
                final_mock += v_mock
            else:
                final_mock += letter_mock
        await msg.channel.send(final_mock + ' <:mock:820984871152648232>')
    elif m.startswith('pls mock'):
        await msg.reply('Já pensaste em usar "pfv mock"? <:uwu:763885294872690688> ')

    else:
        # -----------------------------EMOJIS USERS-----------------------------------------------
        if 'cisco' in m:
            await msg.add_reaction('<:ciscoapoggar:809032623354544178>')
        if 'aoco' in m or 'mdis' in m or 'torcato' in m or "mest" in m:
            await msg.add_reaction('<:ELIMINAR:767703787712282635>')
        if 'aoco' in m or 'mpcp' in m:
            await msg.add_reaction('<:weirdcanas:810630123975868426>')
        if 'amen' in m or 'finalmente' in m or 'politica' in m or 'política' in m:
            await msg.add_reaction('<:zearezar:809032623480504342>')
        if 'java' in m:
            await msg.add_reaction('<:JAVAGAY:799242001173577728>')
        if 'luisinha' in m:
            await msg.add_reaction('<:kuisapoggers:809032623758114876>')
        if 'tiago' in m or 'dvalin' in m or '203766134061793281' in m:
            await msg.add_reaction('<:pogtiago:809032623497805835>')
        if 'mano' in m:
            await msg.add_reaction('<:mano:809032623644082206>')
        if 'pog' in m or 'lezgo' in m or 'lfg' in m or 'lets go' in m:
            await msg.add_reaction('<:poggies:789853745855856660>')
        if 'lima' in m or 'peras' in m or 'gui ' in m or m == 'gui' or ' gui' in m:
            await msg.add_reaction('<:ehehe:761324245308932127>')
        if '247137294459338752' in m:
            await msg.add_reaction('<:perasarezar:809032623825485824>')
        if 'sporting' in m:
            await msg.add_reaction('<:homemsporting:790192696294637578>')
        if 'sex' in m and 'sexta' not in m:
            await msg.add_reaction('🇸')
            await msg.add_reaction('🇪')
            await msg.add_reaction('🇽')
            await msg.add_reaction('🇴')
            await msg.add_reaction('💦')
            await msg.add_reaction('👅')
        if 'ubuntu' in m or 'bash' in m or 'arch' in m or 'linux' in m or 'mint' in m:
            await msg.add_reaction('🤓')
        if 'ramalho' in m:
            await msg.add_reaction('<:OLA:811367924161839174>')
        if 'grr' in m:
            await msg.add_reaction('<:madiana:809032623379972127>')
        if 'frog' in m or '317653551939846144' in m:
            await msg.add_reaction('🐸')
        if 'balta' in m or '<@!100288993039499264>' in m:
            await msg.add_reaction('<:balta:811345262151860265>')
        if 'norberto' in m or 'costa freitas' in m or '<@!190968369791369216>' in m:
            await msg.add_reaction('🇵🇹')
            await msg.add_reaction('🧡')
        if 'flux' in m or '192235561371697152' in m:
            await msg.add_reaction('<:fluxpondera:809032623673442314>')
        if '<:sus:814208083840073820>' in m or 'sus' in m:
            await msg.add_reaction('<:sus:814208083840073820>')
        if 'caralho' in m:
            caralho = ['🇨', '🇦', '🇷', '🅰️', '🇱', '🇭', '🇴']
            for c_var in range(7):
                await msg.add_reaction(caralho[c_var])
        if 'montes' in m or '461439896125702144' in m:
            await msg.add_reaction('<:pogmontes:796338915077652480>')
        if 'pj' in m:
            await msg.add_reaction('<:PJ:819363210243080283>')
        if 'dormir' in m or 'sono' in m or 'sleep' in m:
            await msg.add_reaction('<:residentsleeper:768410966123479043>')
        if 'covid' in m or 'couve' in m or 'corona' in m:
            await msg.add_reaction('😷')
        emoji_miminho = ['<a:hug:812076950155558912>', '<a:beijinho:812078357361066024>',
                         '<a:rena_gorda:812079912960786492>']
        if 'noodle' in m:
            await msg.channel.send('<a:ezgif:812000224217661491>')
        if 'miminho' in m:
            await msg.channel.send(f'{random.choice(emoji_miminho)}')
        if 'trabalho de mest' in m or 'projeto de mest' in m:
            await msg.reply('<:despair:814474380721651732>')
        # ---------------ÚTIL----------------------
        if 'mata-te' in m or 'mata te' in m:
            await msg.delete()
            await msg.channel.send('<:ban:798887475254657074>')
        if 'suicid' in m or 'suícid' in m or 'ero me matar' in m or 'ero morrer' in m or 'ero falecer' in m or 'me matar' in m:
            embed_s = discord.Embed()
            embed_s.title = 'A tua vida importa ♥'
            embed_s.color = 0x04D1FF
            img = ['https://the-gist.org/wp-content/uploads/2020/07/Mental-Health-Emma-Garcia-Melchor_crop.png',
                   'https://www.voicesofyouth.org/sites/voy/files/images/2020-03/3._courtesy_mymindourhumanity_campaign.jpg',
                   'https://workingwise.nz/wp-content/uploads/2020/06/mentalwellbeing.jpg']
            embed_s.set_image(url=random.choice(img))
            embed_s.description = ':telephone: **SOS ESTUDANTE:**  969 554 545 ou 808 200 204 (20h à 1h) \n\n [Mais números e informações - números de saúde mental](http://www.adcl.org.pt/observatorio/servicos.php?titulo=Linhas)'
            await msg.reply(embed=embed_s)
        if 'aulas mieic' in m or 'aulas info' in m:
            embed_aulas = discord.Embed()
            embed_aulas.title = 'Aulas 1ºAno MIEIC'
            embed_aulas.color = 0x00a0a0
            embed_aulas.description = '''\nCMAT \n([seg](https://videoconf-colibri.zoom.us/j/87558364347?pwd=MStyUVpPSlEycmZvbWcrNGF0NnJxZz09) 9:00-10:00 | [qua](https://videoconf-colibri.zoom.us/j/86166483975?pwd=VlRZelRvbjJzMmtXc1dsMDlnNTh0QT09) 10:00-11:00)

            [FIS1](https://videoconf-colibri.zoom.us/j/82373725282?pwd=S1VrNEp4VkZYR2o1TUlPUW1hLzVhZz09)      \n(seg 10:00-11:00 | qua 9:00-10:00)

            [PROG](https://teams.microsoft.com/l/channel/19%3a0a486ea7628247de956d27755601308e%40thread.tacv2/Geral?groupId=b05f83cd-100e-4c31-a797-146513c69887&tenantId=b7821bc8-67cc-447b-b579-82f7854174fc) \n(seg 11:00-12:30 | qui 9:00-10:30)

            [MPCP](https://videoconf-colibri.zoom.us/j/81799571785?pwd=T0U2NEdCTkd6ODhFMmVoTTJ3bHA2dz09) \n(qui 10:30-12:30)

            [MEST](https://videoconf-colibri.zoom.us/j/83335195718?pwd=QW1mTisxZkdFOVM4Y1lHSDRoUU84UT09) \n(qua 11:00-13:00)
            '''

            await msg.reply(embed=embed_aulas)
    await client.process_commands(msg)


@client.command()
async def avatar(ctx, *, avamember: discord.Member = None):
    userAvatarUrl = avamember.avatar_url
    await ctx.send(userAvatarUrl)


@client.command()
async def joined(ctx, *, member: discord.Member):
    j = str(member.joined_at)[8:10] + '-' + str(member.joined_at)[5:7] + '-' + str(member.joined_at)[:4]
    await ctx.send('<@{0.id}> veio ser feupinho na data: ``{1}``'.format(member, j))


@client.command()
async def ping(ctx):
    await ctx.send('pong xd: ``{0}s``'.format(round(client.latency, 3)))


@client.command()
async def membros(ctx):
    await ctx.send(ctx.guild.member_count)


@client.command()
async def dm(ctx, member: discord.Member, *, content):
    channel = await member.create_dm()
    de_dm = '``Mensagem Anónima!``'
    print('recebe: ', member,'\nmanda: ',ctx.author.name)
    img = ['https://i.pinimg.com/originals/63/f0/cf/63f0cfb389116145c4f74b95ee83c0a4.jpg',
           'https://image.dhgate.com/0x0s/f2-albu-g8-M00-B8-01-rBVaV1w1WLqAPtMhABEyHzVVJ9c694.jpg/love-letter-enamel-pin-mail-delivery-turtle.jpg',
           'https://pbs.twimg.com/media/D-K1BWqUIAI7Xx8.jpg',
           'https://i.pinimg.com/564x/57/f8/a5/57f8a50f34f1100304ecbf84ea7fae3a.jpg',
           'https://www.wackyteez.pt/wp-content/uploads/2020/03/0619-you-got-mail-300x300.jpg',
           'https://thumbs.dreamstime.com/b/cute-reindeer-hat-celebration-happy-christmas-stamp-vector-illustration-cute-reindeer-celebration-happy-christmas-stamp-159883847.jpg',
           'https://www.clipartkey.com/mpngs/m/121-1213018_mailbox-mail-delivery-puppy-dog-pet-cute-animal.png',
           'https://i.pinimg.com/474x/1d/46/5e/1d465e140e179041471efa5c8c979b7a.jpg',
           'https://i.pinimg.com/originals/bb/55/87/bb5587c6bf9284c3420abcd2f69e4275.jpg',
           'https://static.boredpanda.com/blog/wp-content/uploads/2019/12/62144452_2261755747276811_7262549243119500388_n-5df0419c10749__700.jpg',
           'https://i.pinimg.com/originals/d7/24/77/d7247773ffec90ae53aff3aa2eeafc9e.jpg',
           'https://media.discordapp.net/attachments/761863843935813672/821416203355947018/doggomail2.jpg?width=507&height=380',
           'https://media.discordapp.net/attachments/761863843935813672/821416206937882683/foxymail.jpg?width=478&height=675',
           'https://media.discordapp.net/attachments/761863843935813672/821416201166651443/doggomail3.jpg?width=508&height=508',
           ]
    embed_dm = discord.Embed()
    embed_dm.set_image(url=random.choice(img))
    embed_dm.title = 'Tens correio! 📬 ' + '\n' + de_dm
    embed_dm.description = '**Mensagem: ** \n"' + content + '"'
    # await channel.send(cute_msg+de_dm+content+'"``')
    await channel.send(embed=embed_dm)
    await ctx.message.delete()


token=os.getenv('TOKEN', '')
client.run(token)