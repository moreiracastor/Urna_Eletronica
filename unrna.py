#Cadastro da senha
import os


def cad_senha(senha, conf_senha):
    while senha != conf_senha:
        conf_senha = input("\nSenha errada, digite novamente:  ")

    return print("Senha cadastrada...\n")


#Cadastro do candidato
def cad_candidato():
    print("Cadastro do Candidato")
    #Pedir a senha de confirmação
    #Pedir o candidato e a chapa
    #Cadastrar num .csv ou bloco de notas
    #Confirmação do voto pela senha digitada

#Lista de participantes
def list_partci(Nome_Do_Arquivo):
        arquivo = Nome_Do_Arquivo

        with open(arquivo, 'r', encoding='UTF-8') as arq:
            txt = arq.read().splitlines()

            for l in txt:
                print(f"* {l}")



#Votação
def votacao(Arq_voto, voto):
    #Abre o arquivo e escreve a chapa no arquivo designado
        with open(Arq_voto, 'a') as arq:
            escrever = arq.write(f"{voto}\n")


#Voto contagem
def voto_contagem(nome_arq, voto):

    with open(nome_arq, 'r', encoding='UTF-8') as arq:
        text = arq.read().splitlines()
              
    return text.count('10')

