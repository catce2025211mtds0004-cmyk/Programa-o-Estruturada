def par_ou_impar(numero):
    return numero % 2 != 0
    
def main():
    numero = int(input().strip())
    print(par_ou_impar(numero))

if __name__ == "__main__":
    main()