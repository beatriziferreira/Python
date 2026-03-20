import math
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

xv = -b / (2 * a)
delta = b**2 - 4*a*c
yv = - delta / (4 * a)

print("Vértice da parábola:")
print("x =", xv)
print("y =", yv)
