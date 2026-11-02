def odd_up_to(n):
    if n == 1:
        return [1]
    if n%2 == 1:
        return odd_up_to(n-1) + [n]
    return odd_up_to(n-1)

def main():
    print(odd_up_to(11))

if __name__ == "__main__":
    main()