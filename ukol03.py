import json

with open('python1-kurz2023/body.json', encoding='utf-8') as file:
    data = json.load(file)

prospech = {}

for jmeno in data:
    if data[jmeno] >= 60:
        prospech [jmeno] = "Pass"
        
    else:
        prospech [jmeno] = "Fail"

with open('prospech.json', mode='w', encoding='utf-8') as file_prospech:  
    json.dump(prospech, file_prospech, indent=2, ensure_ascii=False)       # Čitelnější zápis: odsazení o 2 mezery(indent), nekódovat diakritiku



