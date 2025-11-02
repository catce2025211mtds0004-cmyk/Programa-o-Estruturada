def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b

def main():
    num1 = int(input().strip())
    num2 = int(input().strip())
    op = int(input().strip())
    if op == 1:
        print(soma(num1, num2))
    elif op == 2:
        print(subtracao(num1, num2))
    elif op == 3:
        print(multiplicacao(num1, num2))
    elif op == 4:
        print(divisao(num1, num2))
    else:
        print("Operação inválida")
        
if __name__ == "__main__":
    main()