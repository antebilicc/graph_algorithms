matrica susjedstva:

n X n - n je broj vrhova

citanje grafova, ako je neusmjereni graf onda mora matrica biti simetricna!
**a[i][j] == a[j][i]**, najcesce je 1 (kod neusmjerenog i netezinskog grafa), a kod tezinskog grafa može biti oznaćena drugim brojem, al mora vrijediti ovo!
kod usmjerenoga netriba to biti ->!

također glavna dijagonala je označena sa 0, inaće graf nije jednostavan nego ima petlje!

      a b c d
    a[0      ]
    b[  0    ]
    c[    0  ]
    d[      0]

matrica incidencije:

n X m - n je broj vrhova, a m je broj bridova

gledamo iz kojeg vrha bridovi izlazu i tako stavljamo tezinu brida, inaće ide 1 kod netežinskog grafa

      e1 e2 e3 e4 e5
    a[              ]
    b[              ]
    c[              ]
    d[              ]

pocetak brida kod usmjerenog grafa je -1, a kraj 1, a kod tezinskog grafa -n je pocetak, a n kraj brida!

lista susjedstva:
u pythonu se graf zapisiva ovako:

**graph = {
'a': {'b', 'c'},
'b': {'a', 'c', 'd'},
'c': {'a', 'b', 'd'},
'd': {'b', 'c', 'e'},
'e': {'d'},
}**

gdje su keys vrhovi, a values susjedni vrhovi

provjera npr jesu li neka dva vrha susjedna:
**return vrh1 in graph[vrh2**] ili obrnuto!

print(graph[vrh])

kada dodajemo u graph onda ide:
**graph[v1].add(v2) i
graph[v2].add(v1)**

ali kod usmjerenog grafa je prica drugacija i dodajemo samo njegov smjer odnosno ako recimo v1 -> v2:
**graph[v1].add(v2)**

s time da prvo se mora definirati:
**graph[v1] = set()**


Pajek format:

- ***Verticles** - vrhovi

navodi se broj vrhova n u prvom redu, a onda za svaki vrh pridruženi label ali i ostale informacije(ovisi nekad x, y...), no može biti i bez labela i dodatnih podataka!


- ***Edges** - bridovi, ali neusmjereni

ako je samo oznacen brid npr 1 2 bez trećeg broja onda se uzima težina 1, inaće se uzima težina brida n


- ***Arcs** - usmjereni bridovi

slicno kao edges, ali ovaj ima smjer


Može se još zadati i:

- ***EdgesList** i ***ArcsList** - umjesto jednog brida po retku, u jednom redu možemo navesti sve susjede vhra tako da je a,b,c = a-b, a-c ili za usmjerene a->b, a->c



Primjer za: usmjeren ***ArcsList**
1 2 4 5,  prijevod: [1 -> 2, 1 -> 4, 1 -> 5]
2 3 4 5   prijevod: [2 -> 3, 2 -> 4, 2 -> 5]
3 4         prijevod: [3 -> 4]
4 5         prijevod: [4 -> 5]


- ***Matrix -** matrica susjedstva



**Važno:**

- graf može sadržati i ***Edges** i ***Arcs**, pa onda graf ima i neusmjerene i usmjerene bridove
- može biti i petlja, npr a - a (za neusmjerene) ili a -> a (za usmjerene)
