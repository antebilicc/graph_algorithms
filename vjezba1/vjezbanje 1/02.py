def pretvori_u_hhmmss(sekunde):
    sati = sekunde // 3600
    minute = (sekunde % 3600) // 60
    sekunde = sekunde % 60
    return f"{sati:02d}:{minute:02d}:{sekunde:02d}" 

def main():
    sekunde = 3725
    print(pretvori_u_hhmmss(sekunde))

if __name__ == "__main__":
    main()