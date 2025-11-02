def main():
    pares = 0
    impares = 0
    for i in range(100):
        numero = int(input().strip())
        if numero % 2 == 0:
            pares += 1
        else:
            impares += 1
    
    print(pares)
    print(impares)
    
if __name__ == "__main__":
    main()