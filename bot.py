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
auth = tweepy.OAuthHandler(api_key, api_key_secret, access_token=access_token, access_token_secret=access_token_secret, callback=Response)
api = tweepy.API(auth)

def random_phrase():
    p1 = ["posso voltar quantas vezes for preciso pra te mostrar que não há melhor lugar que o nosso mundo.",
          "eu te amo, ek is lief vir, me dor wo, i love you, ti je zemra ime , gosto de ti, ich hoan dich gear, afekrishalehou, :..:| ..:| |..-.. .::”:.., :.:;, aishiteru, je t’adore, wo ie ni, mi amas vin, je t’aime, te ljubam,Tom ho’ichema… e enfim, eu te amo em todas as linguas.",
          "você é minha cura em meio a toda melancolia.",
          "você é minha sanidade mesmo estando no meio de loucos.",
          "você é o meu céu que jamais nublou.",
          "você é meu inferno congelante.",
          "minha motivação é não ter encontrado respostas p nada.",
          "ainda estou aqui tentando, todos os dias.",
          "mantenha um pouco de fé no seu coração e use para viver amanhã."]
  
    final_phrase = random.choice(p1)
    return final_phrase

while True:
    api.update_status(status=random_phrase().lower())
    print('------------------------------------------')
    print('tweet enviado com sucesso!')
    print('------------------------------------------')
    sleep(1500)