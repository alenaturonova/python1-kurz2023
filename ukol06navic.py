import re

regularni_vyraz_login = re.compile(r"^[a-zA-Z]{6,10}")
login = input("Zadej přihlašovací jméno: ")

hledani_login = regularni_vyraz_login.fullmatch(login)
if hledani_login == False:
    print("Neplatné přihlašovací jméno!")
    exit

regularni_vyraz_heslo = re.compile(r"^(\w|\_|\-|\.|\+|\=){12,30}")
heslo = input("Zadej heslo: ")

hledani_heslo = regularni_vyraz_heslo.fullmatch(heslo)
if hledani_login == False:
    print("Neplatné heslo!")
    exit

regularni_vyraz_email = re.compile(r"^[a-zA-Z0-9_\"?][a-zA-Z0-9._\"\-\+]+[a-zA-Z0-9_\"]+@{1}[a-zA-Z0-9\[][a-zA-Z0-9.\-\[]+\.[a-zA-Z0-9\]]+$")
email = input("Zadej email: ")

hledani_email = regularni_vyraz_email.fullmatch(email)
if hledani_login == False:
    print("Neplatný e-mail!")
    exit

print("Jste úspěšně přihlášen")