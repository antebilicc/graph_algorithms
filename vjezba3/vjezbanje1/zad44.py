def fun(matrica):
    if not matrica:
        return []

    lista = []
    for x in matrica[0]:
        if x <= 0:
            lista.append(0)
        else:
            lista.append(x)
    return [lista] + fun(matrica[1:])
    

def main():
    print(fun([
        [1,2,-12],
        [-23,1,5],
        [7,-9,1]
    ]))

if __name__ == "__main__":
    main()