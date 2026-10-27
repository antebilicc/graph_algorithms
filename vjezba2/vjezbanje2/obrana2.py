#vrati matricu koja se iz dictionary-a koji znamenke broja podjeli i to budu elementi matrice
#npr. za {a:172, b:121, c:132} dobijes [[1, 7, 2], [1, 2, 1], [1, 3, 2]]

def fun(dict):
    matrica = []
    for _, v in dict.items():
        matrica.append([int(d) for d in str(v)]) #ako trebaju stringovi može i cast list(str(v)) umjesto svega unutra
    return matrica

def main():
    dict = {'a': 172, 'b': 121, 'c': 132}
    result = fun(dict)
    print(result)

if __name__ == "__main__":
    main()