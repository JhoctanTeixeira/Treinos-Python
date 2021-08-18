# 2. Faça um programa em Python que leia dados do usuário (nome, sobrenome, idade) adicion em uma lista e imprima seus elementos na tela.
lista_User = []
for i in range(0, 1):
    nome = input("Digite seu nome: ")
    sobrenome = input("Digite seu sobrenome: ")
    idade = input("Digite sua idade: ")
    lista_User.append(nome)
    lista_User.append(sobrenome)
    lista_User.append(idade)
print("Lista nome: {}".format(lista_User))
# print("Seu nome é {} {} e sua idade é {} anos".format(nome, sobrenome, idade))
