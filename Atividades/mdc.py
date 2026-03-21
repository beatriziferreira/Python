def mdc (num1, num2):
    if num1 > num2:
        menor = num2
    else:
        menor = num1
    while menor > 0: # Loop para encontrar o MDC
        if num1 % menor == 0 and num2 % menor == 0: # Verifica se o menor número é divisor de ambos os números
            return menor   # Retorna o MDC encontrado
        menor -= 1 # Decrementa o menor número para verificar o próximo divisor
    return 1 # Retorna 1 se não houver outro divisor comum além de 1
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))  
resultado = mdc(num1, num2)
print(f"O MDC de {num1} e {num2} é: {resultado}")
