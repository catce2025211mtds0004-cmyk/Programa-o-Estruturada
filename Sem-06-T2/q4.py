def converter_idade(idade):
    return idade * 0.5

def main():
    i = float(input().strip())
    convertido = converter_idade(i)
    print(int(convertido))

if __name__ == "__main__":
    main()