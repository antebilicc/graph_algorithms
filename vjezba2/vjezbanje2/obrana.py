#Na grafovi sam imao zadatak sa kvadratom matricom. 
#Trebalo je napravit funkciju koja zbraja stupce kvadratne matrice i trpa ih u dictionary ciji su kljucevi mala slova abecede.
#Na primjer, za [ [1, 2, 7], [9, 3, 5], [7, 6, 0] ]dobijes:
#{a:17, b:11, c:12}

def fun(matrica):
    dictionary = {}
    for i in range(len(matrica)):
        suma = 0
        for j in range(len(matrica)):
            suma += matrica[j][i]
        dictionary[chr(97 + i)] = suma #ord("a") daje 97 
    return dictionary

def main():
    matrica = [ [1, 2, 7], [9, 3, 5], [7, 6, 0] ]
    result = fun(matrica)
    print(result)

if __name__ == "__main__":
    main()