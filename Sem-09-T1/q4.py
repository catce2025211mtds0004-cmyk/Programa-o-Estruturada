def diferenca_menor(n1, n2, n3):
    dif2 = abs(n1 - n2)
    dif3 = abs(n1 - n3)

    if dif2 < dif3:
        return dif2
    else:
        return dif3

def main():
    n1 = int(input().strip())
    n2 = int(input().strip())
    n3 = int(input().strip())
    resultado = diferenca_menor(n1, n2, n3)
    print(resultado)

if __name__ == "__main__":
    main()