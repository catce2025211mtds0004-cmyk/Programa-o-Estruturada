def vogal_consoante_numero_simbolo(char):
    if char.isalpha():
        if char.lower() in 'aeiou':
            return "vogal"
        else:
            return "consoante"
    elif char.isdigit():
        return "número"
    else:
        return "símbolo"
    
def main():
    char = input().strip()
    print(vogal_consoante_numero_simbolo(char))
    
if __name__ == "__main__":
    main()
    