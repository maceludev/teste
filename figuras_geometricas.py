from math import pi

a = float(input("Digite o primeiro valor: "))
b = float(input("Digite o segundo valor: "))
c = float(input("Digite o terceiro valor: "))

area_triang = a*b/2
area_circulo = pi*c**2
area_trapezio = ((a + b) * c) / 2
area_quadrado = b**2
area_retangulo = a*b

print(f"{area_triang:.2f}")
print(f"{area_circulo:.2f}")
print(f"{area_trapezio:.2f}")
print(f"{area_quadrado:.2f}")
print(f"{area_retangulo:.2f}")