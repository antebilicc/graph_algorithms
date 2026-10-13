def sazimanje(s):
    if s == "":
        return ""

    rezultat = ""
    brojac = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            brojac += 1
        else:
            rezultat += s[i - 1] + str(brojac)
            brojac = 1

    rezultat += s[-1] + str(brojac)

    return s, rezultat

def main():
    s, rezultat = sazimanje("aaabbbccdaa")
    print(s, rezultat)

if __name__ == "__main__":
    main()
