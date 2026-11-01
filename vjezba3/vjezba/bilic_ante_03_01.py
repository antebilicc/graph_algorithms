def digit_sum(n):
    if n == 0:
        return 0

    return n % 10 + digit_sum(n // 10)

def count(lst, x):
    if len(lst) == 0:
        return 0

    if lst[0] == x:
        return 1 + count(lst[1:], x)

    return count(lst[1:], x) 

def power(x, n):
    if n == 0:
        return (1, 0)

    if n == 1:
        return (x, 0)

    rezultat, broj = power(x, n // 2)

    rezultat = rezultat * rezultat
    broj += 1

    if n % 2 == 1:
        rezultat = rezultat * x
        broj += 1

    return (rezultat, broj)

def main():
    print(digit_sum(2026))
    print(count([1, 2, 3, 2, 4, 2, 5], 2))

    for n in [10, 100, 1000, 1000000]:
        rezultat, broj = power(2, n)
        print(n, broj, n - 1)

if __name__ == "__main__":
    main()