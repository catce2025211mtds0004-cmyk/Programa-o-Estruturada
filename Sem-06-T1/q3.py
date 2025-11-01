def convertendo_segundos(tempo_em_segundos):
    horas = tempo_em_segundos // 3600
    minutos = (tempo_em_segundos % 3600) // 60
    segundos = tempo_em_segundos % 60
    return horas, minutos, segundos

def main():
    entrada = int(input().strip())
    h, m, s = convertendo_segundos(entrada)
    print(f"{h}:{m}:{s}")
    
if __name__ == "__main__":
    main()