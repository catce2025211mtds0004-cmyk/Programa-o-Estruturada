def gerar_sequencia():
    for i in range(1, 101):
        valor = i * 10
        if i == 100:
            print(f"{valor}.", end="")
        else:
            print(f"{valor}", end=", ")

def main():
    gerar_sequencia()

if __name__ == "__main__":
    main()