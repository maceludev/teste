merrecas = float(input("Digite o valor de merrecas (M$): "))
qnt_cem_merrecas, qnt_cinq_merrecas, qnt_dez_merrecas, qnt_cinco_merrecas, qnt_uma_merreca = 0, 0, 0, 0, 0

if (merrecas >= 100):
    qnt_cem_merrecas = int(merrecas // 100)
    merrecas %= 100
    if (merrecas != 0):
        qnt_cinq_merrecas = int(merrecas // 50)
        merrecas %= 50
        if (merrecas != 0):
            qnt_dez_merrecas = int(merrecas // 10)
            merrecas %= 10
            if (merrecas != 0):
                qnt_cinco_merrecas = int(merrecas // 5)
                merrecas %= 5
                if (merrecas != 0):
                    qnt_uma_merreca = int(merrecas // 1)

print(f"{qnt_cem_merrecas} moeda(s) de M$ 100,00")
print(f"{qnt_cinq_merrecas} moeda(s) de M$ 50,00")
print(f"{qnt_dez_merrecas} moeda(s) de M$ 10,00")
print(f"{qnt_cinco_merrecas} moeda(s) de M$ 5,00")
print(f"{qnt_uma_merreca} moeda(s) de M$ 1,00")

