def fun(lst): #sorta silazno
    if len(lst) == 1:
        return True
    if lst[0] < lst[1]:
        return False 
    return fun(lst[1:])

def main():
    print(fun([5,4,3,2,2,2]))

if __name__ == "__main__":
    main()