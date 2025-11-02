def peso_ideal(sexo, altura):
    if sexo == 1:
        return (72.7 * altura) - 58
    elif sexo == 2:
        return (62.1 * altura) - 44.7
    else:
        return None
    
def main():
    altura = float(input().strip())
    sexo = int(input().strip())    
    print(f"{peso_ideal(sexo, altura):.2f}")
    
if __name__ == "__main__":
    main()
    