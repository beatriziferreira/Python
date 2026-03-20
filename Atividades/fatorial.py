num = int(input("Digite um número: "))
fatorial = 1

if num < 0:
    print("Não existe")
elif num == 0:
    print ("O fatorial de 0 é 1")
else:
    for i in range (1, num + 1):
        fatorial = fatorial * i
    print(f"O fatorial de {num} é {fatorial}")
