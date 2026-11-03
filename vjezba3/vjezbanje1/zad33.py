def fun(s):
    if len(s) == 0:
        return {}

    rezultat = fun(s[1:])

    if s[0] in rezultat:
        rezultat[s[0]] += 1
    else:
        rezultat[s[0]] = 1

    return rezultat
        


def main():
    print(fun("banana"))

if __name__ == "__main__":
    main()  