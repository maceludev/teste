salario_atual = float(input("Digite o salário atual: "))
salario_reaj_ano1 = salario_atual*1.07
salario_reaj_ano2 = salario_reaj_ano1*1.06
salario_reaj_ano3 = salario_reaj_ano2*1.05

print(f"ano 1: {salario_reaj_ano1:.2f}")
print(f"ano 2: {salario_reaj_ano2:.2f}")
print(f"ano 3: {salario_reaj_ano3:.2f}")