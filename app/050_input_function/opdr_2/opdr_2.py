# Opdracht 2 berekeningen
# Naam student:
# Groep:

# Hier komt je code...

print("Je gaat uit eten met Paul, Kees, Marie en Hilda.")
print("Je voegt jezelf toe aan de gastenlijst.")

gasten = ["Jij", "Paul", "Kees", "Marie", "Hilda"]
print ("De gastenlijst is nu:", gasten)

weg = input("wie belt af?")

if weg in gasten:
    gasten.remove(weg)
    print(f"{weg} is van de gastenlijst verwijderd.")
else: 
    print(f"{weg} stond niet op de gastenlijst.")

print("De gastenlijst is nu:", gasten)

print("even later belt George, hij wilt naast Kees zitten!")
index_kees = gasten.index("Kees")
gasten.insert(index_kees + 1, "George")

print("De defininitieve gastenlijst is nu:", gasten)