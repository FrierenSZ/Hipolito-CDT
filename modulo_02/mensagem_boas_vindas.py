'''
Pedir para o usuário escrever o nome e idade
armazenar em variaveis
fazer mais perguntas
armazenar em variaveis
responder perguntas
'''

print("\n---------------------------")
print("Bem Vindo a tela!")
print("\n---------------------------")


nome = input('Qual seu nome? ')
idade = int(input("Qual sua idade? "))


print(f'Olá {nome}, Você tem {idade} anos de idade ')


if idade >= 18:
    print("Aparentemente você é maior de idade ")
else:
    print("Aparentemente você é menor de idade ")



nascimento = (2025 - idade)
print(f'Você nasceu no ano de {nascimento} ') 



altura_pessoa = float(input("Qual sua altura? "))
print('Exemplo: 1.70')
print(f'Você tem {altura_pessoa} de altura! ')
