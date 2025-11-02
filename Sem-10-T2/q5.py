def main():
    valor = float(input().strip())
    for parcelas in range(1, 25):
        prestacao = valor / parcelas
        print(f"{parcelas}x de R$ {prestacao:.2f}")    

if __name__ == "__main__":
    main()