
def media_do_aluno(n1, n2, n3, n4):
    return (n1 + n2 * 2 + n3 * 3 + n4) / 7
    
def conceito(nota):
    if nota >= 9.0:
        return "A"
    elif nota >= 7.5 and nota < 9.0:
        return "B"
    elif nota >= 6.0 and nota < 7.5:
        return "C"
    elif nota >= 4.0 and nota < 6.0:
        return "D"
    elif nota < 4.0:
        return "E"
    else:
        return "Nota inválida"

def main():
    matricula = input().strip()
    n1 = float(input().strip())
    n2 = float(input().strip())
    n3 = float(input().strip())
    n4 = float(input().strip())
    media = media_do_aluno(n1, n2, n3, n4)
    conceito_final = conceito(media)
    print(f"{matricula}")
    print(f"{media:.2f}")
    print(f"{conceito_final}")
    if conceito_final == 'A' or conceito_final == 'B' or conceito_final == 'C':
        print("Aprovado") 
    else:
        print("Reprovado") 
        
if __name__ == "__main__":
    main()