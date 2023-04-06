sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

soucastka_zakaznika = input("Zadej kód součástky: ")
pocet_kusu = int(input("Zadej požadované množství: "))

if soucastka_zakaznika in sklad:

    pocet_soucastek_skladem = sklad[soucastka_zakaznika]
    if pocet_soucastek_skladem < pocet_kusu:
        print(f"Součástka {soucastka_zakaznika} není skladem v požadovaném množství.")
        print(f"Je možné vydat {pocet_soucastek_skladem}.")
        sklad.pop(soucastka_zakaznika)
    else:
        sklad[soucastka_zakaznika] = sklad[soucastka_zakaznika] - pocet_kusu 
        print(f"Součástka {soucastka_zakaznika} je skladem. ")
else:
    print (f"Součástka {soucastka_zakaznika} není skladem.")
            
# print(sklad)