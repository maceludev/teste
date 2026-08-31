dias = int(input("Digite a quantidade de dias trabalhados: "))
diaria = 20.00
imposto = 0.08

pagamento = dias*diaria*(1 - imposto)

print(f"R$ {pagamento:.2f}")