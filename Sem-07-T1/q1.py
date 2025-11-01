def cumprimento(sexo):
    if sexo == 1:
        return "Ilmo Sr."
    elif sexo == 2:
        return "Ilma Sra."
    else:
        return None
    
def main():
    nome = input().strip()
    sexo = int(input().strip())
    print(f"{cumprimento(sexo)} {nome}")
    
if __name__ == "__main__":
    main()