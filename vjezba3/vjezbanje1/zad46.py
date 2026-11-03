def fun(matrica):
    if not matrica or not matrica[0]: #triba stop na prazni redak ili prazna matrica
        return []

    prvi_stupac = [red[0] for red in matrica]
    ostatak = [red[1:] for red in matrica]
    return [prvi_stupac] + fun(ostatak)
    
   

def main():
    print(fun([
        [1,2,-12],
        [-23,1,5],
        [7,-9,1]
    ]))

if __name__ == "__main__":
    main()