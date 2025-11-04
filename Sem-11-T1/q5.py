def projecao(salario, divida):
    mes = 10  
    ano = 2016

    while divida <= salario:    
        mes = mes + 1

        if mes > 12:
            mes = 1
            ano = ano + 1

        divida = divida * 1.15

        if mes == 3:
            salario = salario * 1.05

    return f"{mes}/{ano}"

def main():
    salario = float(input().strip())
    divida = float(input().strip())
    print(projecao(salario, divida))

if __name__ == "__main__":
    main()