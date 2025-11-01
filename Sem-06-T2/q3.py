def preco_maca(valor):
    return 3 * valor

def preco_banana(valor):
    return 2 * valor

def soma(a, b):
    return a + b

def main():
    pm = float(input().strip())
    pb = float(input().strip())
    su = preco_maca(pm)
    sd = preco_banana(pb)
    total = soma(su, sd)
    print(f"{total:.2f}")

if __name__ == "__main__":
    main()