# 6. Faça um programa em Python que solicite ao usuário 10 números inteiros diferentes.
# Mostrar na tela quantos números foram digitados respeitando a solicitação.
# Observação: O usuário somente poderá digitar 10 números.

# numeros = int(input("Digite 10 números inteiros diferentes: "))
listaNum = []
for n in range(0, 10):
    listaNum.append(int(input("Digite um número: ")))
print("-=" * 30)
print("Total de números solicitados:", n)
print(f"Você digitou os números:  {listaNum}")