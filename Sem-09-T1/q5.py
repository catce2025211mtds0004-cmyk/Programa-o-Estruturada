def resto(numero):
    return numero % 5

def calculo_zero(numero):
    return 9 * numero + 7

def calculo_um(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

def calculo_dois(numero):
    return 5 * (numero ** 2) - 3 * numero + 42

def calculo_tres(numero):
    return numero // 10

def calculo_quatro(numero):
    return numero ** 2

def main():
    numero = int(input().strip())
    resultado = resto(numero)
    
    if resultado == 0:
        print(calculo_zero(numero))
    elif resultado == 1:
        print(calculo_um(numero))
    elif resultado == 2:
        print(calculo_dois(numero))
    elif resultado == 3:
        print(calculo_tres(numero))
    elif resultado == 4:
        print(calculo_quatro(numero))

if __name__ == "__main__":
    main()