def casado(numero, nome1):
    if numero == 1:
        conjuge = input().strip()  
        return len(conjuge) + len(nome1)        
    else:
        return len(nome1)

def main():
    nome = input().strip()
    estado_civil = int(input().strip())
    print(casado(estado_civil, nome))

if __name__ == "__main__":
    main()
    