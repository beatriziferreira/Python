termos = int(input("Digite a quantidade de termos da sequência de Fibonacci: "))
a, b = 0, 1
contador = 0
if termos <= 0:
    print("Por favor, digite um número inteiro positivo.")
else:
    print("Sequência de Fibonacci:")
    while contador < termos: # Loop para gerar os termos da sequência de Fibonacci
        print(a, end=" ") # Imprime o termo atual da sequência
        a, b = b, a + b # Atualiza os valores de a e b para os próximos termos da sequência
        contador += 1 # Incrementa o contador para controlar a quantidade de termos gerados
        