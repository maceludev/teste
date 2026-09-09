salario_atual = float(input("Digite o salário atual: "))
salario_reaj_ano1 = salario_atual*((100+7)/100)
salario_reaj_ano2 = salario_reaj_ano1*((100+6)/100)
salario_reaj_ano3 = salario_reaj_ano2*((100+5)/100)

print(f"ano 1: {salario_reaj_ano1:.2f}")
print(f"ano 2: {salario_reaj_ano2:.2f}")
print(f"ano 3: {salario_reaj_ano3:.2f}")