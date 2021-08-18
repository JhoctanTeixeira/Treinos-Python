todas_pessoas = list()
pessoa = dict()
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    pessoa['idade'] = int(input('idade: '))
    pessoa['cidade'] = str(input('cidade: '))
    todas_pessoas.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda S ou N. ')
    if resp == 'N':
        break
print("-=" * 30)
for p in todas_pessoas: 
    for k, v in p.items():
        print(f'{k}: {v}')
    print("-=" * 30)