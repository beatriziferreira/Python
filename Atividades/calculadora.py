print("--CALCULADORA--")
print("Escolha a operação:")
print("1 - Adição")  
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
print("5 - Potenciação")
print("6 - Radiciação")

while True:
    escolha = input("Digite a opção (1/2/3/4/5/6): ")

    if escolha in ['1', '2', '3', '4' , '5' , '6']:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print(f"Resultado: {num1 + num2}")
        elif escolha == '2':
            print(f"Resultado: {num1 - num2}")
        elif escolha == '3':
            print(f"Resultado: {num1 * num2}")
        elif escolha == '4':
            print(f"Resultado: {num1 / num2}")
        elif escolha == '5':
            print(f"Resultado: {num1 ** num2}")
        elif escolha == '6':
            print(f"Resultado: {num1 ** (1/num2)}")
            if num2 == 0:
                print("Erro: Radiciação por zero não é permitida.")
            if num1 < 0:
                print("Erro: Radiciação de número negativo não é permitida.")
        print("Deseja realizar outra operação? (s/n)")
        continuar = input().lower()
        if continuar != 's':
            break
    else:
        print("Opção inválida. Por favor, tente novamente.")