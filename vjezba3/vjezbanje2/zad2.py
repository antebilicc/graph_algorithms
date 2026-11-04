def fun(s):
    if len(s) == 0:
        return 0
    if s[0] in "aeiouAEIOU":
        return 1 + fun(s[1:])
    return fun(s[1:]) 

def main():
    print(fun("stringulja"))

if __name__ == "__main__":
    main()