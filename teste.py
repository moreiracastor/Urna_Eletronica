import unrna as u

arq_voto = 'Dados/votos.txt'
arq_cand = 'Dados/cand.txt'


senha = input("Digite a senha: ")
conf_senha = input("Confirme a senha: ")

#Verificação de senha --> Funciona
u.cad_senha(senha, conf_senha)

#Lista de participantes 
u.list_partci(arq_cand)

#Voto --> Funciona
while True:
    voto = input("Digite a chapa: ")

    u.votacao(arq_voto, voto)

 

