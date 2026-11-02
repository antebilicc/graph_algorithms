def fun(lst, lst2):
    if lst == []:
        return lst2

    if lst2 == []:
        return lst

    if lst[0] < lst2[0]:
        return [lst[0]] + fun(lst[1:], lst2)
    else:
        return [lst2[0]] + fun(lst, lst2[1:])


    
def main():
    print(fun([2,5,8], [1,4,7,7]))

if __name__ == "__main__":
    main()