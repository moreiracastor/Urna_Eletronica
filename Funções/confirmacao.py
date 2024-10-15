#Sistema de confirmação de próxima fase

senha = input("Digite a senha: ")

conf_senha = input("Confirme a senha: ")

while senha != conf_senha:
    conf_senha = input("Senha errada, digite novamente:  ")

print("Senha concluída...")