def fun(s):
    if len(s) == 0:
        return [""]

    rezultat = []

    for i in range(len(s)):
        znak = s[i]
        ostali = s[:i] + s[i+1:]

        for p in fun(ostali):
            rezultat.append(znak + p)

    return rezultat


def main():
    print(fun("abc"))


if __name__ == "__main__":
    main()