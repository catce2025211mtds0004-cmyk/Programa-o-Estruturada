def converter_temperatura(t):
    f = (t * 9/5) + 32
    return f
    
def main():
    no = float(input().strip())
    print(converter_temperatura(no))

if __name__ == "__main__":
    main()