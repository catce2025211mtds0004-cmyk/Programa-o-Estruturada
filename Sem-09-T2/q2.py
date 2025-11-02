def escreva(numero):

    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10

    frase = ""
    qtd_partes = 0

    if centenas == 1:
        frase += "uma centena"
        qtd_partes += 1
    elif centenas == 2:
        frase += "duas centenas"
        qtd_partes += 1
    elif centenas == 3:
        frase += "três centenas"
        qtd_partes += 1
    elif centenas == 4:
        frase += "quatro centenas"
        qtd_partes += 1
    elif centenas == 5:
        frase += "cinco centenas"
        qtd_partes += 1
    elif centenas == 6:
        frase += "seis centenas"
        qtd_partes += 1
    elif centenas == 7:
        frase += "sete centenas"
        qtd_partes += 1
    elif centenas == 8:
        frase += "oito centenas"
        qtd_partes += 1
    elif centenas == 9:
        frase += "nove centenas"
        qtd_partes += 1

    if dezenas > 0:
        if frase != "":
            if unidades > 0:
                frase += ", "
            else:
                frase += " e "
        if dezenas == 1:
            frase += "uma dezena"
        elif dezenas == 2:
            frase += "duas dezenas"
        elif dezenas == 3:
            frase += "três dezenas"
        elif dezenas == 4:
            frase += "quatro dezenas"
        elif dezenas == 5:
            frase += "cinco dezenas"
        elif dezenas == 6:
            frase += "seis dezenas"
        elif dezenas == 7:
            frase += "sete dezenas"
        elif dezenas == 8:
            frase += "oito dezenas"
        elif dezenas == 9:
            frase += "nove dezenas"
        qtd_partes += 1

    if unidades > 0:
        if frase != "":
            frase += " e "
        if unidades == 1:
            frase += "uma unidade"
        elif unidades == 2:
            frase += "duas unidades"
        elif unidades == 3:
            frase += "três unidades"
        elif unidades == 4:
            frase += "quatro unidades"
        elif unidades == 5:
            frase += "cinco unidades"
        elif unidades == 6:
            frase += "seis unidades"
        elif unidades == 7:
            frase += "sete unidades"
        elif unidades == 8:
            frase += "oito unidades"
        elif unidades == 9:
            frase += "nove unidades"
        qtd_partes += 1

    if numero == 0:
        frase = "zero"

    frase += "."    
    return frase


def main():
    numero = int(input().strip())
    print(escreva(numero))
    
if __name__ == "__main__":
    main()