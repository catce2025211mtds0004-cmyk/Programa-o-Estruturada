def a_vista(valor):
    return valor * (1 - 0.09)

def em_5x(valor):
    return valor / 5

def em_10x(valor):
    valor_com_juros = valor * (1 + 0.17)
    return valor_com_juros / 10


def main():
    valor = float(input().strip())
    print(f"{a_vista(valor):.2f}")
    print(f"{em_5x(valor):.2f}")
    print(f"{em_10x(valor):.2f}")
    
    
if __name__ == "__main__":
    main()