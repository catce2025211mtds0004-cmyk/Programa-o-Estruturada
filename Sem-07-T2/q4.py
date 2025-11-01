def signo(data, mes):
    if (data >= 21 and mes == 3) or (data <= 19 and mes == 4):
        return "Áries"
    elif (data >= 20 and mes == 4) or (data <= 20 and mes == 5):
        return "Touro"
    elif (data >= 21 and mes == 5) or (data <= 21 and mes == 6):
        return "Gêmeos"
    elif (data >= 22 and mes == 6) or (data <= 22 and mes == 7):
        return "Câncer"
    elif (data >= 23 and mes == 7) or (data <= 22 and mes == 8):
        return "Leão"
    elif (data >= 23 and mes == 8) or (data <= 22 and mes == 9):
        return "Virgem"
    elif (data >= 23 and mes == 9) or (data <= 22 and mes == 10):
        return "Libra"
    elif (data >= 23 and mes == 10) or (data <= 21 and mes == 11):
        return "Escorpião"
    elif (data >= 22 and mes == 11) or (data <= 21 and mes == 12):
        return "Sagitário"
    elif (data >= 22 and mes == 12) or (data <= 19 and mes == 1):
        return "Capricórnio"
    elif (data >= 20 and mes == 1) or (data <= 18 and mes == 2):
        return "Aquário"
    elif (data >= 19 and mes == 2) or (data <= 20 and mes == 3):
        return "Peixes"
    else:
        return "Data inválida"

def main():
    data = int(input().strip())
    mes = int(input().strip())
    print(signo(data, mes))

if __name__ == "__main__":
    main()