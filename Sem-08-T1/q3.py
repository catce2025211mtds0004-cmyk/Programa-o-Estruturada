def maior_numero(a, b):
    if a > b:
        return a
    else: 
        return b

def menor_numero(a, b):
    if a < b:
        return a
    else:
        return b

def main():
    n1 = int(input().strip())
    n2 = int(input().strip())
    maior = maior_numero(n1, n2)
    menor = menor_numero(n1, n2)
    n3 = int(input().strip())
    maior = maior_numero(maior, n3)
    menor = menor_numero(menor, n3)
    n4 = int(input().strip())
    maior = maior_numero(maior, n4)
    menor = menor_numero(menor, n4)
    n5 = int(input().strip())
    maior = maior_numero(maior, n5)
    menor = menor_numero(menor, n5)
    print(maior)
    print(menor)
    
if __name__ == "__main__":
    main()