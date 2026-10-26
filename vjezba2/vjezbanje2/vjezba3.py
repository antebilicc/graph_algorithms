def main():
    d = {"name": "John", "age": 30, "city": "New York"}
    print(d.get("name")) #printa value ključa

    print(d.get("country", "Not Found")) #printa default value b ako ključ a ne postoji get(a,b) za razliku od d["country"] koji bi bacio error

    print(d.keys()) #printa sve ključeve
    print(d.values()) #printa sve vrijednosti
    print(d.items()) #printa sve parove ključ-vrijednost

    d["country"] = "USA" #dodaje novi par ključ-vrijednost
    print(d)

    d["country"] = "Canada" #mijenja vrijednost postojećeg ključa
    print(d)

    d.update({"age": 31, "city": "Los Angeles", "army": "US Army"}) #mijenja više vrijednosti odjednom i dodaje nove ako ne postoje
    print(d)

    d.pop("armyy", 0) #uklanja par ključ-vrijednost po ključu, a ako ne postoji sa definiranjem default vrijednosti ne mjenja dictionary
    print(d)

    x = d.setdefault("gender", "male") #dodaje novi par ključ-vrijednost ako ključ ne postoji, a ako postoji ne mjenja vrijednost
    y = d.setdefault("age", 25) 
    print(x) #printa vrijednost ključa gender
    print(y) #printa vrijednost ključa age
    print(d)

    
if __name__ == "__main__":
    main()