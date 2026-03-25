def dec_p_binario(num):
    if num == 0:
        return '0'
    elif num == 1:
        return '1'
    else:
        return dec_p_binario(num // 2) + str(num % 2) # Chama a função recursivamente para o quociente da divisão por 2 e concatena o resto (0 ou 1) à string resultante
    
num = int(input("Digite um número decimal: "))
binario = dec_p_binario(num)
print(f"O número decimal {num} em binário é: {binario}")
