import tweepy
from datetime import datetime
from httplib2 import Response
import schedule
import time

# twitter developers api connect
bearer_token = ''
api_key = ''
api_key_secret = ''
access_token = ''
access_token_secret = ''
print("chaves de autenticação, ok.")
time.sleep(3)

# connect
auth = tweepy.OAuthHandler(api_key, api_key_secret, access_token=access_token,
                           access_token_secret=access_token_secret, callback=Response)
api = tweepy.API(auth)
print("autenticação com a API, ok.")
time.sleep(3)

tweets = [
    (datetime(year=2023, month=6, day=16, hour=22, minute=5),
     "me sinto bem apesar de tudo.", None),
    (datetime(year=2023, month=6, day=16, hour=22, minute=28),
     "um desenho de um joguinho que eu gosto.", "C:/Users/dream/Desktop/bot/IMG.jpg"),
    (datetime(year=2023, month=6, day=16, hour=22, minute=32), "saudades.", None)
]


def post_tweet(tweet, photo_path=None):
    if photo_path is None:
        api.update_status(tweet)
    else:
        media = api.media_upload(photo_path)
        api.update_status(status=tweet, media_ids=[media.media_id])


for post_datetime, tweet, photo_path in tweets:
    schedule.every().day.at(post_datetime.strftime("%H:%M")).do(
        post_tweet, tweet, photo_path or None)


def random_phrase():
    p1 = ["posso voltar quantas vezes for preciso pra te mostrar que não há melhor lugar que o nosso mundo.",
          "eu te amo, ek is lief vir, me dor wo, i love you, ti je zemra ime , gosto de ti, ich hoan dich gear, afekrishalehou, :..:| ..:| |..-.. .::”:.., :.:;, aishiteru, je t’adore, wo ie ni, mi amas vin, je t’aime, te ljubam,Tom ho’ichema… e enfim, eu te amo em todas as linguas.",
          "ela é minha cura em meio a toda melancolia.",
          "ela é o meu céu que jamais nublou.",
          "você é meu inferno congelante.",
          "minha motivação é não ter encontrado respostas pra nada.",
          "ainda estou aqui tentando, todos os dias.",
          "mantenha um pouco de fé no seu coração e use para viver amanhã.",
          '"aqui é onde você precisa estar."',
          "e quem disse que você é um em um milhão? você é bem melhor que isso.",
          "eu queria que você fosse a última coisa na minha mente.",
          "queria que você fosse a razão de eu fechar meus olhos.",
          "became my downfall-",
          "eu estarei bem se você nunca me perguntar.",
          "cair é facil, mas só há um caminho para cima.",
          "você pode ir se realmente quiser.",
          "despedidas continuam me arrastando para baixo e eu estou lutando contra a gravidade...",
          "eu acho engraçado que as pessoas que mais amamos são as que mais nos machucam.",
          "eu sei que isso nunca vai acabar.",
          "parece um fim que não consigo substituir.",
          "nós envelhecemos mas nunca aprendemos a dizer adeus.",
          "eu só quero viver como os do passado.",
          "talvez assim eles se lembrem de mim quando eu partir.",
          "eu posso falar qualquer merda que eu quiser porque eu não ligo mais pra nada.",
          "eu vou continuar te amando por mais que você duvide.",
          "eu penso sobre como é se sentir exausto tão jovem.",
          "eu só quero morrer antes do meu coração começar a falhar.",
          "e mesmo se não existir um deus, no dia que eu morrer, ao menos saberei que vivi o paraíso.",
          "eu queria que ela fosse a minha yellow.",
          "start again.",
          "você sempre tem uma segunda chance, você poderia ir para casa e começar novamente.",
          "você pode pode ser o que quiser.",
          "você tem um coração afetuoso e uma mente linda. <3",
          "anchor.",
          "você pode ser a âncora de alguém.",
          "suas lágrimas, um mar para eu nadar.",
          "isso é tudo que sempre fomos?",
          "não vá, você é metade de mim agora. :(",
          "finding hope 2 a.m",
          "tudo que somos está despencando pelo espaço numa queda interminável.",
          "uma vida em repetição.",
          "o que você não sabe pode te assustar.",
          "seja honesto sobre seus sentimentos.",
          "vamos sair daqui e viver como nos filmes.",
          "cause i'm a fucking mess sometimes",
          "morrendo lentamente.",
          "eu não posso amar quando eu não consigo nem me amar.",
          "my atlantis, we fall",
          "eu te amei como Van Gogh amou as estrelas e você me amou como ele amou a vida.",
          "eden - death of a dream - https://youtu.be/TwsZidGLzWY",
          "novo amor - anchor - https://youtu.be/Ajsgx9yDY-0",
          "in another life i would make you stay...",
          "amei você no seu pior momento...",
          "talvez noutra vida ou na próxima vida, seríamos finalmente eu e você. talvez o universo nos desse outra chance.",
          "você não fazia parte do plano.",
          "aquilo que te faz diferente é o que te torna especial.",
          "e se o felizes para sempre existisse?",
          "e um dia você poderá me encontrar onde o mar se derrama nas estrelas.",
          "eu ficarei bem se você ficar.",
          "a vida não é nada além de um sonho.",
          "stargazing",
          "como faz pra voltar no tempo?",
          "simplesmente ela.",
          "tu te tornas eternamente responsável por aquilo que cativas.",
          "Imagine ser o suficiente para alguém.",
          "falling in love is painful.",
          "me compre comida e eu vou te amar para sempre.",
          "50% idk 50% idc.",
          "guarde seus sentimentos para alguém que realmente se importa com você.",
          "você disse que estaria lá por mim. mas onde está você agora?",
          "reza a lenda que conversas tarde da noite com amigos podem ser uma das melhores terapias.",
          "me abraça pfv.........",
          "apenas algo que me faça lembrar do que esqueci.",
          "há lugares incríveis mesmo em tempos sombrios e se não houver, você pode ser aquele lugar, com infinitas capacidades.",
          "desde que você chegou minhas borboletas pararam de voar e agora elas dançam.",
          "e a convicção de que mágoas e tristezas que parecem eternas não duram para sempre.",
          "why would you ever kiss me?",
          "why not me?",
          "me + you = <3",
          "cânticos 4:7",
          "no one, no one.",
          "se tu me cativas, precisaremos um do outro, você será para mim o único no mundo.",
          "engraçado que existem bilhões de galáxias, eu não sei a dimensão desse número. mas eu fico feliz por ter encontrado vocês no mesmo lugar.",
          "desisto de você, mas ainda torço por nós dois.",
          "a minhã mão longe da tua mão segue orbitando o nada na vasta solidão.",
          "toda poesia do mundo não te definiria.",
          "tantas estrelas no céu e eu fui me apaixonar por uma cadentekkkk."]

    final_phrase = random.choice(p1)
    return final_phrase

print("todos os tweets foram checados até aqui, tudo ok.")
time.sleep(2)

print("iniciando loop de postagem...")
time.sleep(1)
while True:
    try:
        schedule.run_pending()
        tweets = api.user_timeline()
        print("o ID do tweet é:\n", tweets[0].id)
        print("---"*5)
        print("o último tweet postado foi:\n", tweets[0].text)
        print("---"*5)
    except Exception as e:
        print(f"erro: {e}")
        continue
    time.sleep(120)