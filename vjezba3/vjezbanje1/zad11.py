def fun(str):
    if len(str) == 0:
        return str
    
    return fun(str[1:]) + str[0]

def main():
    print(fun("Python"))


if __name__ == "__main__":
    main()