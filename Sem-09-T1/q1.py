def verifica(a, b, c):
    if a == b and b == c:
        return "Todos os valores são iguais"
    elif a == b or a == c or b == c:
        return "Existem dois valores iguais e um diferente"
    else:
        return "Todos os valores são diferentes"


def main():
    n1 = int(input().strip())
    n2 = int(input().strip())
    n3 = int(input().strip())
    print(verifica(n1, n2, n3))
    
if __name__ == "__main__":
    main()