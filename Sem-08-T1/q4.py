def mediana(a, b, c, d, e):
    return (a + b + c + d + e) / 5


def maior_nota(n1, media):
    if n1 > media:
        return True
    else:
        return False


def main():
    a = float(input().strip())
    b = float(input().strip())
    c = float(input().strip())
    d = float(input().strip())
    e = float(input().strip())

    media = mediana(a, b, c, d, e)
    print(f"{media:.2f}")

    if maior_nota(a, media):
        print(f"{a:.2f}")
    if maior_nota(b, media):
        print(f"{b:.2f}")
    if maior_nota(c, media):
        print(f"{c:.2f}")
    if maior_nota(d, media):
        print(f"{d:.2f}")
    if maior_nota(e, media):
        print(f"{e:.2f}")


if __name__ == "__main__":
    main()
