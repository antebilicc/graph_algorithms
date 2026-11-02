def fun(lst):
    if lst == []:
        return []
    
    if len(lst) == 1:
        return [lst[0]]
    
    if lst[0] != lst[1]:
        return [lst[0]] + fun(lst[1:])
    
    return fun(lst[1:])

def main():
    print(fun([1,1,1,1,2,2,2,3,6,6,1,9,6,8,2,2]))

if __name__ == "__main__":
    main()