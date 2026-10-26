from ucitavanje import fun
from provjere import kvadratna, simetricna, stohasticka
from operacije import  mnozenje, dijagonale, transponiraj

def main():
  A = fun("datoteka.txt")
  B = fun("datoteka2.txt")

  print(A)
  print(B)

  print(kvadratna(A))
  print(simetricna(A))
  print(stohasticka(A))

  print(kvadratna(B))
  print(simetricna(B))

  print(mnozenje(A,B))
  print(dijagonale(A))
  print(dijagonale(B))
  print(transponiraj(A))


if __name__ == "__main__":
    main()