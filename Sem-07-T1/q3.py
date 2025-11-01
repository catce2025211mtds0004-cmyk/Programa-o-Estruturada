def cor_do_sinal(cor):
    if cor == "E":
        return "Pare"
    elif cor == "A":
        return "Atenção"
    elif cor == "V":
        return "Siga"
    else:
        return "Cor inválida"
    
def main():
    cor = input().strip().upper()
    print(cor_do_sinal(cor))
    
if __name__ == "__main__":
    main()
    