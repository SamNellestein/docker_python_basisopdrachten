# Opdracht 2 tekstbestanden
# Naam student:
# Groep:

import random

def main():
    
    geheim_getal = random.randint(1, 100)
    pogingen = 0

    print("Raad mijn geheime getal (tussen 1 en 100). Typ 'stop' om te stoppen.")
    while True:
        poging = input("Raad mijn geheime getal\n").strip()
        if poging.lower() == 'stop':
            print("Je hebt het spel gestopt.")
            return

        
        try:
            getal = int(poging)
        except ValueError:
            print("Voer een geldig heel getal in tussen 1 en 100.")
            continue

        if not (1 <= getal <= 100):
            print("Gebruik een getal tussen de 1 en 100.")
            continue

        pogingen += 1

        if getal < geheim_getal:
            print("hoger")
        elif getal > geheim_getal:
            print("lager")
        else:
            print(f"Je hebt het getal geraden het is {geheim_getal}!")
            print(f"Je hebt het in {pogingen} keer gedaan")
            break

if __name__ == "__main__":
    main()
