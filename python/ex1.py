# print("1. Dada a lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52] faca um programa em Python que: ")

lista = [12, -2, 4, 8, 29, 45, 78, 36, -17, 2, 12, 8, 3, 3, -52] 

print("a) imprima o maior elemento ")

maior_elemento = 0
for num in lista:
    if  (maior_elemento == 0 or num > maior_elemento):
        maior_elemento = num     
print("Maior elemento: {}".format(maior_elemento))
print("Usando max")
max_elemento = max(lista)
print("Maior elmento: {}".format(max_elemento))
print("-=" * 30)

print("b) imprima o menor elemento ")
menor_elemento = 0
for num in lista:
    if  (menor_elemento == 0 or num < menor_elemento):
        menor_elemento = num
print("Menor elemento: {}".format(menor_elemento))
print("Usando min")
min_elemento = min(lista)
print("Menor elemento: {}".format(min_elemento))
print("-=" * 30)

print("c) imprima os numeros pares")
lista_pares = []
for pares in lista:
    if pares % 2 == 0:
        lista_pares.append(pares)
        lista_pares.sort()
print("Números pares encontrados na lista: {}".format(lista_pares))      
print("-=" * 30)

print("d) imprima o numero de ocorrências do primeiro elemento da lista ")
ocorrencias = lista.count(12)
print("Ocorrências do primeiro elemento:  {} ".format(ocorrencias))
print("-=" * 30)

print("e) imprima a media dos elementos ")
media = sum(lista)/len(lista)
print("Média da lista : ", media) 
print("-=" * 30)

print("f) imprima a soma dos elementos de valor negativo ")
soma_negativo = 0
for n in lista:
    if n < 0:
        soma_negativo += n
print("Soma dos elementos negativos é igual a : {}".format(soma_negativo))
print("-=" * 30)