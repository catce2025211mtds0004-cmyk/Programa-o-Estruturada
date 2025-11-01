def maior_valor(lista):
    return max(lista)

def menor_valor(lista):
    return min(lista)

def media(lista):
    return sum(lista) / len(lista)


def main():
    valores = [int(input().strip()) for _ in range(5)]
    print(maior_valor(valores))
    print(menor_valor(valores))
    print(f"{media(valores):.2f}")
    

if __name__ == "__main__":
    main()