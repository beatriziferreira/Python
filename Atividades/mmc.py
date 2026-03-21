def mmc(x, y): # Função para calcular o MMC de dois números
    if x > y:
        maior = x
    else:
        maior = y
    while True: # Loop infinito para encontrar o MMC
        if maior % x == 0 and maior % y == 0: # Verifica se o maior número é múltiplo de ambos os números
            mmc = maior # Armazena o MMC encontrado
            break # Encerra o loop quando o MMC é encontrado
        maior += 1 # Incrementa o maior número para verificar o próximo múltiplo
    return mmc # Retorna o MMC encontrado
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
resultado = mmc(num1, num2)
print(f"O MMC de {num1} e {num2} é: {resultado}")
