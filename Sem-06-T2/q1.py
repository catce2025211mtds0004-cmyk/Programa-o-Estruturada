def quantidade_de_caracteres(texto):
    return len(texto)

def main():
    entrada = input().strip()
    print(quantidade_de_caracteres(entrada))
    
if __name__ == "__main__":
    main()