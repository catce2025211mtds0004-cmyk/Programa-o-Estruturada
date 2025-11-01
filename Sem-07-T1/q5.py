def notas(n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    if n3 > 8:
        media += 1                
    return min(media, 10)

def main():
    n1 = float(input().strip())
    n2 = float(input().strip())
    n3 = float(input().strip())
    print(f"{notas(n1, n2, n3):.2f}")
    
if __name__ == "__main__":
    main()