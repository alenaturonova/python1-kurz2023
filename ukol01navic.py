jmeno_a_prijmeni = input("Zadej svoje jméno a příjmení: ").strip()

print(jmeno_a_prijmeni)

print(jmeno_a_prijmeni.upper())        #vše velké
print(jmeno_a_prijmeni.lower())        #vše malé
      
#ze zadaných hodnot vytvořit seznam
seznam = (jmeno_a_prijmeni.split(" "))

#první písmeno velké, ostatní malé
print(seznam[0][0].upper() + seznam[0][1:].lower() +
       " " + seznam[1][0].upper() + seznam[1][1:].lower())

#pouze iniciály z jména a příjmení
print(seznam[0][0].upper() + ". " + seznam[1][0].upper() + ".")

#Zkrácení jména na jeden znak, pokud je jméno delší jak 5 znaků

if len(seznam[0]) < 5:
    print(seznam[0][0].upper() + seznam[0][1:].lower() + " " 
          + seznam[1][0].upper() + seznam[1][1:].lower())
else:
    print(seznam[0][0].upper() + ". " + seznam[1][0].upper() + 
          seznam[1][1:].lower())
    