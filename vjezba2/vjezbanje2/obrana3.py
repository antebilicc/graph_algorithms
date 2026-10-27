def fun(dictionary):
    matrica = []
    for _,v in dictionary.items():
        suma = sum(v)
        matrica.append(list(str(suma)))
    return matrica     
    
def main():
    dictionary= {
        "a":[23, 56, 78],
        "b":[12, 45, 67],
        "c":[34, 56, 78],
        "d":[12, 34, 56],
        "e":[23, 45, 67]
    }
    print(fun(dictionary))

if __name__ == "__main__":
    main()