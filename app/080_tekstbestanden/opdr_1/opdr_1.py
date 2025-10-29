# Opdracht 1 while-loops
# Naam student:
# Groep:

# Jouw code komt hier

vragen = [ 
    "wat vind je van de huidige regering?", 
    "wat vind je van de Python-lessen tot nu toe?",
    "wat vind je de mooiste stad van Nederland?"
]

antwoorden = []
for v in vragen: 
    a = input(v + " ")
    antwoorden.append(a.strip())


with open("enquete_results.txt", "a", encoding="utf-8") as f:
    for i in range(len(vragen)):
        f.write(vragen[i] + "\n")
        f.write(antwoorden[i] + "\n")
    f.write("\n")  # lege regel tussen enquêtes