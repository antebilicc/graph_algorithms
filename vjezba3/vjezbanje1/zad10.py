def hanoi(n, a, b, c):
    if n == 1:
        return [(a, c)]

    potezi = []

    potezi += hanoi(n - 1, a, c, b)
    potezi.append((a, c))
    potezi += hanoi(n - 1, b, a, c)

    return potezi


def main():
    print(hanoi(3, "A", "B", "C"))
    print(len(hanoi(10, "A", "B", "C")))


if __name__ == "__main__":
    main()