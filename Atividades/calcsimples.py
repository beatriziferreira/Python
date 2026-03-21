num1 = float(input("Digite um numero para adiçao: "))
num2 = float(input("Digite outro numero para adiçao: "))
soma_resultado = num1 + num2
print(f"Soma =  {soma_resultado}")

num3 = float(input("Digite o dividendo para divisão: "))
num4 = float(input("Digite o divisor para divisão: "))
if num4 == 0:
    print("Erro")
else:
    div_resultado = num3 / num4
    print(f"Divisão = {div_resultado}")