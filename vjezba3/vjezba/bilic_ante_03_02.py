from math import log2
from mjerenje import measure

def halvings(n):
    if n == 1:
        return 0

    return 1 + halvings(n // 2)


def linear_search(lst, x):
    for i in range(len(lst)):
        if lst[i] == x:
            return i

    return -1


def binary_search(lst, x):
    lijevo = 0
    desno = len(lst) - 1
    lst.sort()

    while lijevo <= desno:
        sredina = (lijevo + desno) // 2

        if lst[sredina] == x:
            return sredina

        elif x < lst[sredina]:
            desno = sredina - 1

        else:
            lijevo = sredina + 1

    return -1

def in_set(s, x):
    return x in s

def main():
    print(halvings(10))
    print(linear_search([1, 2, 3, 4, 5], 3))
    print(binary_search([1, 2, 3, 4, 5], 3))
    print(in_set({1, 2, 3, 4}, 3))

    for n in [10, 100, 1000, 10000, 100000, 1000000]:
        lst = list(range(n))
        s = set(lst)

        x = n

        h = halvings(n)
        log = log2(n)

        t1 = measure(linear_search, lst, x)
        t2 = measure(binary_search, lst, x)
        t3 = measure(in_set, s, x)

        print(n, h, log, t1, t2, t3)


if __name__ == "__main__":
    main()