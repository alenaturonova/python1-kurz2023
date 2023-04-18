import json

with open('python1-kurz2023/body.json', encoding='utf-8') as file1:
    data1 = json.load(file1)

with open('python1-kurz2023/body_ukolnavic.json', encoding='utf-8') as file2:
    data2 = json.load(file2)

prospech1 = {}

for jmeno in data2:
    bonus_body = data2[jmeno]
    data1[jmeno] = data1[jmeno] + bonus_body

for jmeno in data1:
    celkove_body = data1[jmeno]

    if celkove_body <= 29:
        mark = 5
    elif celkove_body <= 49:
        mark = 4
    elif celkove_body <= 69:
        mark = 3
    elif celkove_body <= 89:
        mark = 2
    else:
        mark = 1
       
    prospech1[jmeno] = mark

with open('prospech1.json', mode='w', encoding='utf-8') as file_prospech:  
    json.dump(prospech1, file_prospech, indent=2, ensure_ascii=False) 
