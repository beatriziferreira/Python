frutas = ["maçã", "banana", "uva"]

print(frutas[0])  # Imprime "maçã"
print(frutas[1])  # Imprime "banana"
print(frutas[2])  # Imprime "uva"
frutas.append("laranja")  # Adiciona "laranja" à lista
print(frutas)  # Imprime a lista atualizada com "laranja"

while True:
    fruta = input("Digite o nome de uma fruta (ou 'sair' para encerrar): ")
    if fruta.lower() == "sair":
        break
    frutas.append(fruta)
    print("Fruta adicionada! Lista atualizada:", frutas)