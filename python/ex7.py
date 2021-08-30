
print("Faça um programa em Python que leia as listas acima e mostre na tela: \n")
print("-=" * 30)

listaA = [9,8,7,1,6,2,4,3,1,6]
listaB = [8,6,4,9,5,3,1,3,6,4]

print("a) Quais números aparecem na listaA e não aparecem na listaB. \n")
sA = set(listaA)
sB = set(listaB)
print("Numeros na lista:", sA.difference(sB))
print("-=" * 30)

print("b) Quais números se repetem na listaA. \n")
print("c) Quais números se repetem na listaB. \n")
def pegar_repetidos(lista):
    repetidos = []
    numeros = []
    
    for i in lista:
        if i in numeros:
            repetidos.append(i)
        else:
            numeros.append(i)
    return repetidos
print(f"Repetidos listaA:  {pegar_repetidos(listaA)}")
print(f"Repetidos listaB :  {pegar_repetidos(listaB)}")
print("-=" * 30)

print("d) Uma única lista com todos os números da listaA e da listaB. \n")

print("Lista única com todos elementos:", listaA + listaB)
print("-=" * 30)

print("e) Uma única lista com todos os números da listaA e da listaB (não mostrar se tiver número repetido). \n")
lA = set(listaA)
lB = set(listaB)
print("Lista única sem numeros repetidos", lA.symmetric_difference(lB))
print("-=" * 30)