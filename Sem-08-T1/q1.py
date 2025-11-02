from datetime import date

def data_atual():
    dia = int(input())
    mes = int(input())
    ano = int(input())
    data_hoje = date(ano, mes, dia)
    return data_hoje

def data_nascimento():
    dia = int(input())
    mes = int(input())
    ano = int(input())
    data_de_nascimento = date(ano, mes, dia)
    return data_de_nascimento
    

def main():
    hoje = data_atual()
    nascimento = data_nascimento()
    idade = hoje.year - nascimento.year - ((hoje.month, hoje.day) < (nascimento.month, nascimento.day))
    print(idade)
    
if __name__ == "__main__":
    main()