def podredeni(team, osoba):
    rezultat = []

    for p in team[osoba]:
        rezultat.append(p)
        rezultat += podredeni(team, p)

    return rezultat

def razine(team, osoba):
    rezultat = 0

    for p in team[osoba]:
        rezultat = max(rezultat, razine(team, p))

    return rezultat + 1

def main():
    team = {'ana': ['bruno', 'cvita'], 'bruno': ['duje', 'ema'],
            'cvita': ['frane'], 'duje': [], 'ema': [],
            'frane': ['goran'], 'goran': []}
    print(podredeni(team, "ana"))

    print(razine(team, "ana"))

    
    
if __name__ == "__main__":
    main()