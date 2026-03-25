import math

print("Fórmula do número imaginário: a + bi")
a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))

z = complex(float(a), float(b))

# módulo
r = math.sqrt(z.real**2 + z.imag**2)

# argumento (em radianos)
theta = math.atan2(z.imag, z.real)

if a >= 0 and b >= 0:
    graus = theta * (180 / math.pi)  # Quadrante I
elif a <= 0 and b >= 0:
    graus = theta * (180 / math.pi) # Quadrante II
elif a <= 0 and b <= 0:
    graus = 360 + (theta * (180 / math.pi))  # Quadrante III
else:  # a >= 0 and b < 0
    graus = 360 + (theta * (180 / math.pi))  # Quadrante IV


print(f"\nNúmero complexo: {z}")
print("Forma trigonométrica:")
print(f"{r:.2f} * (cos({graus:.1f}°) + i*sin({graus:.1f}°))")
print("Ou em radianos:")
print(f"{r:.2f} * (cos({theta:.2f}) + i*sin({theta:.2f}))")