def fun(d):
    if len(d) == 0:
        return None

    if len(d) == 1:
        return list(d.keys())[0]
    prvi = list(d.keys())[0]
    ostali = dict(list(d.items())[1:])
    
    najbolji = fun(ostali)

    if d[prvi] > d[najbolji]:
        return prvi
    
    return najbolji
    

def main():
    print(fun({'ana': 7, 'bruno': 9, 'cvita': 4, 'duje': 8}))

if __name__== "__main__":
    main()