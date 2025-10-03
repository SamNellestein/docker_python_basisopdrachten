# Opdracht 3 condities
# Naam student:
# Groep:




normale_toegangsprijs = 12.50
kortings_percentages = {"baby": 100, "kinderen": 50, "volwassenen": 0, "ouderen": 30}
leeftijd = {"baby": (0, 2), "kinderen": (3, 18), "volwassenen": (19, 64), "ouderen": (65, 150)}


leeftijd_input = int(input("Geef je leeftijd in aantal jaar(en): "))

groep = None 
for groep_naam, (min_leeftijd, max_leeftijd) in leeftijd.items():
    if min_leeftijd <= leeftijd_input <= max_leeftijd:
        groep = groep_naam
        break

korting = kortings_percentages[groep]

te_betalen = normale_toegangsprijs * (1 - korting / 100)

print(f"U behoort tot de groep: {groep}")
print(f"U krijgt {korting}% korting")
print(f"U moet €{te_betalen:.2f} betalen")

exit()