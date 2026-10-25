from matrica import read_matrix, print_matrix

def otok_info(matrix):
    broj_kopna = 0
    najvisa_tocka = (0, 0, 0)

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] > 0:
                broj_kopna += 1

                if matrix[i][j] > najvisa_tocka[0]:
                    najvisa_tocka = (matrix[i][j], i, j)

    return broj_kopna, najvisa_tocka

def nadi_vrhove(matrix):
    vrhovi = []
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[i]) - 1):
            height = matrix[i][j]

            if height > 0:
                if (height > matrix[i - 1][j] and height > matrix[i + 1][j] and height > matrix[i][j - 1] and height > matrix[i][j + 1]):
                    vrhovi.append((i, j))
            
    return vrhovi

def prebroji_obalu(matrix):
    broj_obale = 0
    for i in range(1, len(matrix) - 1):
        for j in range(1, len(matrix[i]) - 1):
            if matrix[i][j] > 0:
                if (matrix[i - 1][j] == 0 or matrix[i + 1][j] == 0 or matrix[i][j - 1] == 0 or matrix[i][j + 1] == 0):
                    broj_obale += 1

    return broj_obale

def karta(matrix):
    mapa = []
    for i in range(len(matrix)):
        redak = ""

        for j in range(len(matrix[i])):
            if matrix[i][j] == 0:
                redak += "~"

            elif (matrix[i - 1][j] == 0
                  or matrix[i + 1][j] == 0
                  or matrix[i][j - 1] == 0
                  or matrix[i][j + 1] == 0):
                redak += "#"

            else:
                redak += "o"

        mapa.append(redak)
    return mapa 

def main():
    matrix = read_matrix("otok.txt")
    print_matrix(matrix)

    broj_kopna, najvisa_tocka = otok_info(matrix)
    print(broj_kopna, najvisa_tocka)

    vrhovi = nadi_vrhove(matrix)
    print(vrhovi)

    obala = prebroji_obalu(matrix)
    print(obala)

    mapa = karta(matrix)
    for redak in mapa:
        print(redak)

if __name__ == "__main__":
    main()