merrecas = float(input("Digite o valor de merrecas (M$): "))

qnt_cem = merrecas // 100
qnt_cinq = merrecas % 100 // 50
qnt_dez = merrecas % 100 % 50 // 10
qnt_cinco = merrecas % 100 % 50 % 10 // 5
qnt_um = merrecas % 100 % 50 % 10 % 5

print(f"{qnt_cem} moeda(s) de M$ 100,00")
print(f"{qnt_cinq} moeda(s) de M$ 50,00")
print(f"{qnt_dez} moeda(s) de M$ 10,00")
print(f"{qnt_cinco} moeda(s) de M$ 5,00")
print(f"{qnt_um} moeda(s) de M$ 1,00")

