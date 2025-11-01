distancia = int(input().strip())
velocidade = int(input().strip())
horas_totais = distancia / velocidade 
dias = horas_totais // 24
horas = horas_totais % 24
print(f'{int(dias)} dias e {int(horas)} horas')