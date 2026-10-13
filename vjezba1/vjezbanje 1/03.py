def password_check(password):
    lista = []
    if len(password) < 8:
        lista.append("barem 8 znakova")
    if not any(c.isupper() for c in password):
        lista.append("veliko slovo")
    if not any(c.islower() for c in password):
        lista.append("maleno slovo")
    if not any(c.isdigit() for c in password):
        lista.append("znamenka")
    return lista


def main():
    print(password_check("abcd1234!A"))

if __name__ == "__main__":
    main()