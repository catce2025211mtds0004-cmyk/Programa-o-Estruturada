def main():
    soma = 0
    contador = 0

    while True:
        numero = int(input().strip())
        if numero == 0:
            break
        soma += numero
        contador += 1

    media = soma / contador
    print(f"{media:.2f}")

if __name__ == "__main__":
    main()