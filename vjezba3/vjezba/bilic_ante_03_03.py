from matrica import read_matrix, print_matrix
from mjerenje import measure

def zbroj(m1, m2):
    l1 = (len(m1), len(m1[0]))
    l2 = (len(m2), len(m2[0]))
    
    if l1 != l2:
        return None
    
    m3 = [[0 for _ in range(l1[1])] for _ in range(l1[0])]
    
    for i in range(len(m1)):
        for j in range(len(m1[0])):
            m3[i][j] = m1[i][j] + m2[i][j]
            
    return m3

def pomnozi(m1, m2):
    if len(m1[0]) != len(m2):
        return None

    m3 = [[0 for _ in range(len(m2[0]))]
          for _ in range(len(m1))]

    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):
                m3[i][j] += m1[i][k] * m2[k][j]

    return m3

def identity(n):
    m = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        m[i][i] = 1

    return m

def matrix_power(a, k):
    if k == 0:
        return identity(len(a))

    rezultat = a

    for i in range(k - 1):
        rezultat = pomnozi(rezultat, a)

    return rezultat

def fast_matrix_power(a, k):
    if k == 0:
        return identity(len(a))

    if k == 1:
        return a

    pola = fast_matrix_power(a, k // 2)
    rezultat = pomnozi(pola, pola)

    if k % 2 == 1:
        rezultat = pomnozi(rezultat, a)

    return rezultat

def test_vremena(p):

    for k in [100, 1000, 10000, 100000]:
        t1 = measure(matrix_power, p, k)
        t2 = measure(fast_matrix_power, p, k)

        print(k, t1, t2)

def main():
    a1 = read_matrix("A1.txt")
    b1 = read_matrix("B1.txt")
    a2 = read_matrix("A2.txt")
    b2 = read_matrix("B2.txt")
    p = read_matrix("P.txt")

    print_matrix(zbroj(a1, a2))

    print_matrix(pomnozi(b1, a1))

    print_matrix(matrix_power(p, 3))

    print_matrix(matrix_power(p, 100))

    print_matrix(fast_matrix_power(p, 100))

    test_vremena(p)
  
    
if __name__ == "__main__":
    main()
    