# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

invoer = input("voer minimaal 5 objecten in, gescheiden door komma's: ")

objecten = [item.strip() for item in invoer.split(",")]

objecten.sort(reverse=True)

print(objecten)

