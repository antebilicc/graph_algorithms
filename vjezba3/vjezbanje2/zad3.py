def fun(matrica):
    if len(matrica) == 0:
        return True
    
    for i in range(len(matrica[0])):
        if matrica[0][i] < 0:
            return False
        
    return fun(matrica[1:])

def fun2(matrica):
    if len(matrica) == 0:
        return 0
    najveci = max(matrica[0])
    return max(najveci, fun2(matrica[1:]))

def main():
    print(fun(
        [[1, 2, 3], 
         [0, 5, 6], 
         [7, 0, -1]]))

    print(fun2(
        [[1, 2, 3],
         [0, 5, 6],
         [7, 0, -1]]))

if __name__ == "__main__":
    main()