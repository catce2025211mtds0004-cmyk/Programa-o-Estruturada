def numeros_pares(numero):
    digitos = str(numero)
    pares = 0
    for digito in digitos:
        if int(digito) % 2 == 0:
            pares += 1
    return pares

def main():
    numero = int(input().strip())
    print(numeros_pares(numero))
    
if __name__ == "__main__":
    main()