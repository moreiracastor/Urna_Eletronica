#Sistema para a Votação

#Impressão no terminal dos participantes e as chapas
print("* Lista de participantes:")
with open('cand.txt', 'r', encoding='UTF-8') as arq:
    txt = arq.read().splitlines()

    for l in txt:
        print(f"* {l}")


#Voto
voto = input("* Digite a chapa do seu candidato: ")#Chapa do candidato para a votação

#Abre o arquivo e escreve a chapa no arquivo designado
with open('votos.txt', 'a') as arq:
    escrever = arq.write(voto)

print("Votação concluida")


