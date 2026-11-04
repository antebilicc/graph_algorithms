def fun(lst, lst2):
    if lst2 == []:
        return lst

    if lst == []:
        return lst2
    
    return [lst2[-1]] + [lst[-1]] + fun(lst[:-1], lst2[:-1]) 


def main():
    print(fun([1, 2, 3], [4, 5, 6, 7, 8, 9]))

if __name__ == "__main__":
    main()