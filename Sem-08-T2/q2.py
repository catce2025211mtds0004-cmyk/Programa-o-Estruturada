def somar_digitos(numero):
    if not (0 < numero < 100000):
        return -1
    else:
        if numero < 10:
            soma = numero
        elif numero < 100:
            soma = (numero // 10) + (numero % 10)
        elif numero < 1000:
            soma = (numero // 100) + ((numero // 10) % 10) + (numero % 10)
        elif numero < 10000:
            soma = (numero // 1000) + ((numero // 100) % 10) + ((numero // 10) % 10) + (numero % 10)
        elif numero < 100000:
            soma = (numero // 10000) + ((numero // 1000) % 10) + ((numero // 100) % 10) + ((numero // 10) % 10) + (numero % 10)
        else:  
            soma = 1
        return soma

def main():
    numero = int(input().strip())
    print(somar_digitos(numero))
    
if __name__ == "__main__":
    main()