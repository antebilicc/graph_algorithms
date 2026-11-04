def fun(n):
    if n < 2: 
        return n
    return fun(n - 1) + fun(n - 2)

def main():
    print(fun(10))

if __name__ == "__main__":
    main()
    