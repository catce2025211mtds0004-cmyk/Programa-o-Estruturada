def texto_em_data(texto):
    dia = int(texto[:2])
    mes = int(texto[2:4])
    ano = int(texto[4:])
    return dia, mes, ano

def data_valida(dia, mes, ano):   
    if mes < 1 or mes > 12:
        return False

    if dia < 1:
        return False
    
    if mes in [1, 3, 5, 7, 8, 10, 12]:
        return dia <= 31
   
    elif mes in [4, 6, 9, 11]:
        return dia <= 30

    elif mes == 2:

        bissexto = (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
        if bissexto:
            return dia <= 29
        else:
            return dia <= 28

    return False

def main():
    data = input().strip()
    dia, mes, ano = texto_em_data(data)
    print(data_valida(dia, mes, ano))

if __name__ == "__main__":
    main()