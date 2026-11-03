def fun(d, k):
    if len(d) == 0:
        return 0

    prvi = list(d.keys())[0]
    ostali = dict(list(d.items())[1:])

    if d[prvi] > k:
        return 1 + fun(ostali, k)

    return fun(ostali, k)
    

def main():
    print(fun({'ana': 7, 'bruno': 9, 'cvita': 4, 'duje': 8}, 5))

if __name__== "__main__":
    main()