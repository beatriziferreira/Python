def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        return "Erro: Divisão por zero não é permitida."
    return a / b
print("--CALCULADORA--")
print("Escolha a operação:")
print("1 - Adição")  
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

while True:
    escolha = input("Digite a opção (1/2/3/4): ")

    if escolha in ['1', '2', '3', '4']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print(f"Resultado: {adicao(num1, num2)}")
        elif escolha == '2':
            print(f"Resultado: {subtracao(num1, num2)}")
        elif escolha == '3':
            print(f"Resultado: {multiplicacao(num1, num2)}")
        elif escolha == '4':
            print(f"Resultado: {divisao(num1, num2)}")

        print("Deseja realizar outra operação? (s/n)")
        continuar = input().lower()
        if continuar != 's':
            break
    else:
        print("Opção inválida. Por favor, tente novamente.")