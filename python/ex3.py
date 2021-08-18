# 3. Faça um programa em Python que leia 4 notas, mostre as notas e a média na tela.
nota1 = float(input("Primeira nota: "))
nota2 = float(input("Segunda nota: "))
nota3 = float(input("Terceira nota: "))
nota4 = float(input("Quarta nota: "))
media = (nota1 + nota2 + nota3 + nota4) / 4
        
print("Tirando {:.1f}, {:.1f}, {:.1f} e {:.1f} a média é {:.1f}".format(nota1, nota2, nota3, nota4, media))