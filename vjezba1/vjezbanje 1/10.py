def u_binarno(broj):
    string = ""
    while broj > 0:
        string = str(broj % 2) + string
        broj = broj // 2
    return string

def u_broj(str):
    broj = 0
    for i in range(len(str)):
        broj = broj * 2 + int(str[i])
    return broj

def main():
    str = u_binarno(13)
    print(str)
    broj = u_broj(str)
    print(broj)

if __name__ == "__main__":
    main()