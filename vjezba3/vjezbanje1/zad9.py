def stepenice(n):
    if n == 0:
        return (1, 1)

    if n == 1:
        return (1, 2)

    a = stepenice(n - 1)
    b = stepenice(n - 2)

    return (a[0] + b[0], a[1] + b[1] + 1)

def stepenice_memo(n, memorija=None):
    if memorija is None:
        memorija = {}

    if n in memorija:
        return (memorija[n][0], 0)

    if n == 0:
        memorija[n] = (1, 1)
        return (1, 1)

    if n == 1:
        memorija[n] = (1, 2)
        return (1, 2)

    a = stepenice_memo(n - 1, memorija)
    b = stepenice_memo(n - 2, memorija)

    nacini = a[0] + b[0]
    pozivi = a[1] + b[1] + 1

    memorija[n] = (nacini, pozivi)

    return (nacini, pozivi, memorija)

def stepenice3(n):
    if n == 0:
        return (1, 1)

    if n == 1:
        return (1, 2)

    if n == 2:
        return (2, 4)

    a = stepenice3(n - 1)
    b = stepenice3(n - 2)
    c = stepenice3(n - 3)

    return (a[0] + b[0] + c[0],
            a[1] + b[1] + c[1] + 1)


def main():
    print(stepenice(10))
    print(stepenice_memo(10))
    print(stepenice3(10))


if __name__ == "__main__":
    main()