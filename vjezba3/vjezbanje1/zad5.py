def fun(a, b):
    if b == 0:
        return a

    return fun(b, a % b)

def main():
    print(fun(462, 1071))

if __name__ == "__main__":
    main()