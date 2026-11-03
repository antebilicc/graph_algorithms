def fun(d):
    if len(d) == 0:
        return {}

    prvi = list(d.keys())[0]
    ostali = dict(list(d.items())[1:])

    return {d[prvi]: prvi} | fun(ostali)


def main():
    print(fun({'ana': 7, 'bruno': 9, 'cvita': (4,5,6), 'duje': 8}))

if __name__== "__main__":
    main()