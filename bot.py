# a phrase bot
# by dream
# add libs
from time import sleep
from httplib2 import Response
import tweepy
import random

# twitter developers api connect
bearer_token = ''
api_key = ''
api_key_secret = ''
access_token = ''
access_token_secret = ''

# connect
auth = tweepy.OAuthHandler(api_key, api_key_secret, access_token=access_token,
access_token_secret=access_token_secret, callback=Response)
api = tweepy.API(auth)


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
          "queria que você fosse a razão de fechar meus olhos.",
          "became my downfall",
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
          "aaaaaaa."]

    final_phrase = random.choice(p1)
    return final_phrase


while True:
    api.update_status(status=random_phrase().lower())
    print('------------------------------------------')
    print('tweet enviado com sucesso!')
    print('------------------------------------------')
    sleep(1500)
