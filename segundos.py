horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))

horas_seg = horas * 3600
minutos_seg = minutos * 60

total_seg = horas_seg + minutos_seg + segundos

print(total_seg)