def fun(d):
    kljuci = list(d.keys())

    if len(kljuci) == 0:
        return 0

    najveci = d[kljuci[0]]

    ostatak = fun(dict(list(d.items())[1:]))

    if najveci < ostatak:
        najveci = ostatak

    return najveci

def main():
    print(fun({'ana': 7, 'bruno': 9, 'cvita': 4, 'duje': 8}))
if __name__ == "__main__":
    main()