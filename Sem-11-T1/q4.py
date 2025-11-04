def invertido(numero):
    inverso = 0
    while numero > 0:
        resto = numero % 10        
        inverso = inverso * 10 + resto 
        numero = numero // 10  
    return inverso

def main():
    numero = int(input().strip())
    print(invertido(numero))
    
if __name__ == "__main__":
    main()