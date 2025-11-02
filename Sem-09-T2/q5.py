def veredito(numero):
    if numero == 2:
        return "Suspeito"
    elif numero == 3 or numero == 4:
        return "Cúmplice"
    elif numero == 5:
        return "Assassino"
    else:
        return "Inocente"

def main():
    r1 = input().strip().upper()
    r2 = input().strip().upper()
    r3 = input().strip().upper()
    r4 = input().strip().upper()
    r5 = input().strip().upper()

    total = 0
    if r1 == "S":
        total = total + 1
    if r2 == "S":
        total = total + 1
    if r3 == "S":
        total = total + 1
    if r4 == "S":
        total = total + 1
    if r5 == "S":
        total = total + 1

    resultado = veredito(total)
    print(resultado)

if __name__ == "__main__":
    main()
