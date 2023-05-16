class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = int(najete_km)
        self.dostupne = True

    def pujc_auto(self):
        if self.dostupne == True:
            print("Potvrzuji zapůjčení vozidla")
            self.dostupne = False
        else:
            print("Vozidlo není k dispozici")

    def getInfo(self):
        print (f"Auto {self.typ_vozidla} registrační značky {self.registracni_znacka}.")

 
auto_peugeut = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
auto_skoda = Auto("1P3 4747", "Škoda Octavia", 41253 )

vypujceni_auta = input("Jaké vozidlo si přejete půjčit? Máme v nabídce Peugeot a Škoda.")

if vypujceni_auta == "Škoda":
        auto_skoda.pujc_auto()
        auto_skoda.getInfo()
elif vypujceni_auta == "Peugeot":
        auto_peugeut.pujc_auto()
        auto_peugeut.getInfo()
else:
        print("Zadejte jiné auto.")

vypujceni_auta = input("Jaké vozidlo si ještě přejete půjčit? Máme v nabídce Peugeot a Škoda.")

if vypujceni_auta == "Škoda":
        auto_skoda.pujc_auto()
        auto_skoda.getInfo()
elif vypujceni_auta == "Peugeot":
        auto_peugeut.pujc_auto()
        auto_peugeut.getInfo()
else:
        print("Zadejte jiné auto.")









