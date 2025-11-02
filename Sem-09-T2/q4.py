def quilo_frutas(morango, macas):
    return morango + macas

def preco_bruto_morango(morango):
    if morango > 5:
        return 2.2 * morango
    else:
        return 2.5 * morango
    
def preco_bruto_maca(maca):
    if maca > 5:
        return 1.5 * maca
    else:
        return 1.8 * maca
    
def calcula_frutas(morango, macas):
    return preco_bruto_maca(macas) + preco_bruto_morango(morango)

def desconto(morangos, macas):
    if quilo_frutas(morangos, macas) > 8 or calcula_frutas(morangos, macas) > 25:
        return calcula_frutas(morangos, macas) * 0.90
    else:
        return calcula_frutas(morangos, macas)    
    
def main():
    morangos = float(input().strip())
    macas = float(input().strip())
    print(f"{desconto(morangos, macas):.2f}")

if __name__ == "__main__":
    main()