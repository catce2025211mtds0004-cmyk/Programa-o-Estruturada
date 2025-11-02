from datetime import date

def ler_data():
    dia = int(input())
    mes = int(input())
    ano = int(input())
    data = date(ano, mes, dia)
    return data

def data_recente(data1, data2):
    if data1 > data2:
        return data1
    else:
        return data2
    
def main():
    data1 = ler_data()
    data2 = ler_data()    
    recente = data_recente(data1, data2)
    data_formatada = f"{recente.day}/{recente.month}/{recente.year}"
    print(f"{data_formatada}")
    
if __name__ == "__main__":
    main()
    