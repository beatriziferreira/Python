nota1 = float(input("Digite um número: ")) * 2
nota2 = float(input("Digite outro número: ")) * 3
nota3 = float(input("Digite mais um número: ")) * 5
media = (nota1 + nota2 + nota3) / 10
print("A média total é: ", media)
if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")
