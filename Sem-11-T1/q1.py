def retorno_dobro(deposito, taxa):
    anos = 0
    inicial = deposito
    
    while deposito < inicial * 2:
        deposito += deposito * taxa        
        anos += 1
    return anos

def main():
    deposito = float(input().strip())
    taxa = float(input().strip()) / 100
    print(retorno_dobro(deposito, taxa))
    

if __name__ == "__main__":
    main()