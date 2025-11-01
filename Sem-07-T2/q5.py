def sequencia_maior(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        if num2 > num3:
            return f"{num3}\n{num2}\n{num1}"
        if num3 > num2:
            return f"{num2}\n{num3}\n{num1}"
    if num2 > num1 and num2 > num3:
        if num1 > num3:
            return f"{num3}\n{num1}\n{num2}"
        if num3 > num1:
            return f"{num1}\n{num3}\n{num2}"
    if num3 > num1 and num3 > num2:
        if num1 > num2:
            return f"{num2}\n{num1}\n{num3}"
        if num2 > num1:
            return f"{num1}\n{num2}\n{num3}"

def main():
    num1 = int(input().strip())
    num2 = int(input().strip())
    num3 = int(input().strip())
    resultado = sequencia_maior(num1, num2, num3)
    print(resultado)
    
if __name__ == "__main__":
    main()