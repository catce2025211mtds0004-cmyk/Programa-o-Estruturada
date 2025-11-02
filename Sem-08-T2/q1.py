def soma(alg):
    if alg % 2 == 0:
        return alg + 5
    else:
        return alg + 8

def main():
    numero = int(input().strip())
    print(soma(numero))

if __name__ == "__main__":
    main()
    