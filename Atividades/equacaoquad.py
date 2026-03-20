import math
a = float(input("Digite o a: "))
b = float(input("Digite o b: "))
c = float(input("Digite o c: "))

delta = b**2 - 4*a*c
if delta > 0:
    raiz1 = (-b + math.sqrt(delta)) / (2*a)
    raiz2 = (-b - math.sqrt(delta)) / (2*a)
    print(f"Raiz 1 = {raiz1}")
    print(f"Raiz 2 = {raiz2}")
elif delta < 0:
    parte_real = -b / (2*a)
    parte_imaginaria = math.sqrt(abs(delta)) / (2*a)
    print(f"Raiz 1: {parte_real} + {parte_imaginaria}i")
    print(f"Raiz 2: {parte_real} - {parte_imaginaria}i")
else:
    raiz = -b / (2*a)
    print(f"Raiz: {raiz}")
