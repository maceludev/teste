duracao = int(input("Digite a duração da chamada em minutos: "))
total = 1.15
if (duracao <= 3):
    print(f"R$ {total:.2f}")
else:
    pagamento = total + 0.26*(duracao - 3)
    print(f"R$ {pagamento:.2f}")