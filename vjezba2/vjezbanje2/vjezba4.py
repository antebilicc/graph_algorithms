def main():
    m = [[1, 2, 3], 
               [4, 5, 6], 
               [7, 8, 9]]  #matrica je lista lista
    print([m[0][2]])

    #postoje matrice susjedstva također gdje se ide: i simetricni su
    #   A B C
    # A
    # B
    # C

    #ne kvadratna matrica jer ima 2 elementa a u svakom elementu još 3 elementa
    m2 = [
        [2,3,4], 
        [1,4,5]]

    for r in m2:
        for c in r:
            print(c, end=" ") 
        print()

    for i in range(len(m2)):
        for j in range(len(m2[i])):
            print(m2[i][j], end=" ")
        print()

    print(je_simetricna(m))
    print(je_simetricna(m2))

def je_simetricna(A):
    if len(A) != len(A[0]):
        return False

    for i in range(len(A)):
        for j in range(len(A)):
            if A[i][j] != A[j][i]:
                return False

    return True

if __name__ == "__main__":
    main()