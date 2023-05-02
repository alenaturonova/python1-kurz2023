from statistics import mean     # funkce mean - průměr

teploty = [
    [2.1, 5.2, 6.1, -0.1],
    [2.2, 4.8, 5.6, -1.0],
    [3.3, 6.5, 5.9, 1.2],
    [2.9, 5.6, 6.0, 0.0],
    [2.0, 4.6, 5.5, -1.2],
    [1.0, 3.2, 2.1, -2.0],
    [0.4, 2.7, 1.3, -2.8]
]

prumerne = [round (mean(den), 1) for den in teploty]
print(prumerne)

ranni = [den [0] for den in teploty]
print(ranni)

nocni = [den [-1] for den in teploty]
print(nocni)

poledne_noc = [[den [1], den [3]] for den in teploty]
print(poledne_noc)


# ukol BONUS:
teploty_dny = [
    ["pondělí", 2.1, 5.2, 6.1, -0.1],
    ["úterý", 2.2, 4.8, 5.6, -1.0],
    ["středa", 3.3, 6.5, 5.9, 1.2],
    ["čtvrtek", 2.9, 5.6, 6.0, 0.0],
    ["pátek", 2.0, 4.6, 5.5, -1.2],
    ["sobota", 1.0, 3.2, 2.1, -2.0],
    ["neděle", 0.4, 2.7, 1.3, -2.8]
]

# průměrná teplota z teploty_dny (zaokrouhleno na 3 desetinná místa)
# dict comprehension
zaokrouhlene_teploty = {den[0]: round(sum(den[1:]) / len(den[1:]), 3) for den in teploty_dny}
print(zaokrouhlene_teploty)