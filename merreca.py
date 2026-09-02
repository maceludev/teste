merrecas = float(input("Digite o valor de merrecas (M$): "))

qnt_cem = merrecas // 100
qnt_cinq = merrecas % 100 // 50
qnt_dez = merrecas % 100 % 50 // 10
qnt_cinco = merrecas % 100 % 50 % 10 // 5
qnt_um = merrecas % 100 % 50 % 10 % 5

qnts = [qnt_cem, qnt_cinq, qnt_dez, qnt_cinco, qnt_um]

moedas = [100, 50, 10, 5, 1]

for i in range(len(qnts)):
    print(f"{int(qnts[i])} moeda(s) de M$ {int(moedas[i])},00")


