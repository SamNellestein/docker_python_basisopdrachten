# Opdracht 4 condities
# Naam student:
# Groep:



toppings = [("olijven", 4.50), ("kaas", 3.50), ("salami", 3.00), ("pepperoni", 2.00) , ("ansjovis", 2.50)]
beschikbare_toppings = [topping[0] for topping in toppings]

keuze = input(f"Maak een keuze uit onze toppings: {beschikbare_toppings} \n")

beschikbare_toppings = [topping[0] for topping in toppings]
if keuze in beschikbare_toppings:
    prijs = next(prijs for naam, prijs in toppings if naam == keuze)
    print(f"De prijs van {keuze} is €{prijs:.2f}")
else:
    print(f"Sorry, {keuze} is niet beschikbaar als topping.")


