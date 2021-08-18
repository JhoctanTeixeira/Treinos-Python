# 4. Faça um programa utilizando um dict (dicionário) que leia dados de entrada do usuário. O
# usuário deve entrar com os dados de uma pessoa como nome, idade e cidade onde mora.
# Após isso, você deve imprimir os dados como o exemplo abaixo:
# nome: João
# idade: 20
# cidade: São Paulo

pessoas = dict()
pessoas['nome'] = str(input('Nome: '))
pessoas['idade'] = int(input('idade: '))
pessoas['cidade'] = str(input('cidade: '))
print("-=" * 30)
for k, v in pessoas.items():
    print(f'{k}: {v}')
