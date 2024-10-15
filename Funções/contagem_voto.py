import os


with open('votos.txt', 'r', encoding='UTF-8') as arq:
    text = arq.read().splitlines()
              
              
print(text.count('10'))

