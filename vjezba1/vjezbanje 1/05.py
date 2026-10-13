
def kaprekar(n):
    koraci = 0

    while n != 6174:
        znamenke = f"{n:04d}"

        uzlazno = int("".join(sorted(znamenke)))
        silazno = int("".join(sorted(znamenke, reverse=True)))

        n = silazno - uzlazno
        print (n)
        koraci += 1

    return koraci

def main():
    n = 3524
    rez = kaprekar(n)
    print(rez)

if __name__ == "__main__":
    main()