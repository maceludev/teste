from math import pi

altura = float(input("Digite a altura do cone: "))
raio = float(input("Digite o raio do cone: "))

volume = (1/3)*pi*raio**2*altura

print(f"{volume:.2f}")