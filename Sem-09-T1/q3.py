def geometria(base, altura):
    if base == altura:
        return "QUADRADO"
    else:
        perimetro = 2 * (base + altura)
        area = base * altura
        return perimetro, area

def main():
    base = float(input().strip())
    altura = float(input().strip())
    resultado = geometria(base, altura)
    if resultado == "QUADRADO":
        print("QUADRADO")
    else:
        perimetro, area = resultado
        print(f"{perimetro:.0f} - {area:.0f}")

if __name__ == "__main__":
    main()