def binom(n, k):
    if k == 0 or k == n:
        return (1, 1)

    b1 = binom(n - 1, k - 1)
    b2 = binom(n - 1, k)

    return (b1[0] + b2[0], b1[1] + b2[1] + 1)

def binom2(n, k, memorija=None):
    if memorija is None:
        memorija = {}

    if (n, k) in memorija:
        return memorija[(n, k)], 0, memorija

    if k == 0 or k == n:
        memorija[(n, k)] = 1
        return 1, 1, memorija

    b1, p1, memorija = binom2(n - 1, k - 1, memorija)
    b2, p2, memorija = binom2(n - 1, k, memorija)

    rezultat = b1 + b2
    pozivi = p1 + p2 + 1

    memorija[(n, k)] = rezultat

    return rezultat, pozivi, memorija


def main():
    print(binom(20, 10))
    print(binom2(20, 10))

if __name__ == "__main__":
    main()