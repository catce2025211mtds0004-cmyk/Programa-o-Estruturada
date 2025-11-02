def calculo_imc(peso, altura):
    return peso / (altura ** 2)

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso"
    elif 18.5 <= imc < 25:
        return "Peso normal"
    elif 25 <= imc < 30:
        return "Sobrepeso"
    elif 30 <= imc < 35:
        return "Obeso leve"
    elif 35 <= imc < 40:
        return "Obeso moderado"
    else:
        return "Obeso mórbido"
    
def main():
    peso = float(input())
    altura = float(input())
    imc = calculo_imc(peso, altura)
    classificacao = classificar_imc(imc)
    print(f"{imc:.2f}")    
    print(classificacao)
    
if __name__ == "__main__":
    main()