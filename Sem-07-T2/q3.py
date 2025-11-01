def numeros_pares(numero):

    digitos = str(numero)
    pares = 0
    impares = 0

    for digito in digitos:
        if int(digito) % 2 == 0:
            pares += 1
        else:
            impares += 1

    if impares == 0:
        return "Nenhum dígito é ímpar."
    
    if impares == 1:
        return "Apenas um dígito é ímpar."
    
    else:
        return "Os dois dígitos são ímpares."


def main():
    numero = int(input().strip())
    print(numeros_pares(numero))
    
if __name__ == "__main__":
    main()