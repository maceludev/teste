from math import pi

altura = float(input("Digite a altura do cilindro: "))
raio = float(input("Digite o raio do cilindro: "))

volume = pi*raio**2*altura

print(f"{volume:.2f}")