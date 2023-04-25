def je_cislo_platne(telefonni_cislo):
    telefonni_cislo = telefonni_cislo.replace(" ", "")    # odstranění mezer z čísla
    """
    Zkontroluje zadané telefonní číslo jestli je platné - kontrola jestli má 9 míst, nebo 13 (i s předvolbou)
    """
    if len(telefonni_cislo) == 9:
        return True
    elif len(telefonni_cislo) ==13 and telefonni_cislo[0:4] == "+420":
        return True
    else:
        return False
        
def vypocet_ceny_sms(text_sms):
    """
    Vypočítá počet sms dle zadaného textu. Jedna SMS = 180 znaků. A vypočítá cenu za celou zprávu.
    """
    delka_sms = len(text_sms)
    pocet_sms = delka_sms // 180
    zbytek_sms = delka_sms % 180
    if zbytek_sms == 0:
        return pocet_sms * 3
    else:
        return (pocet_sms + 1) * 3


telefonni_cislo = input("Zadejte telefonní číslo, kam chcete SMS odeslat: ")
je_platne = je_cislo_platne(telefonni_cislo)
if je_platne:
    text_sms = input("Zadejte SMS zprávu: ")
    cena_sms = vypocet_ceny_sms(text_sms)
    print(f"Cena SMS je: {cena_sms} Kč.")
else:
    print("Zadané číslo není platné.")









