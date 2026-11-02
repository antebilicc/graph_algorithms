def fun(lst):
    if lst == []:
        return []
    if lst[0] % 2 == 0:
        return [lst[0]] + fun(lst[1:])

    return fun(lst[1:]) 

def main():
    print(fun([5,2,8,3,6]))

if __name__ == "__main__":
    main()