# Opdracht 1 lists
# Naam student:
# Groep:

# Vraag de gebruiker om een nummer
nummer = int(input("Voer een nummer in (0-3): "))



mylist = []
dict_1 = {"id": 0, 'voornaam': 'Jan', 'achternaam': 'Jansen'}
dict_2 = {"id": 1, 'voornaam': 'Piet', 'achternaam': 'Pietersen'}
dict_3 = {"id": 2, 'voornaam': 'Klaas', 'achternaam': 'Klaassen'}
dict_4 = {"id": 3, 'voornaam': 'Marie', 'achternaam': 'Jansen'}

mylist.append(dict_1)
mylist.append(dict_2)       
mylist.append(dict_3)
mylist.append(dict_4)


# Print de volledige naam van de persoon van de gekozen nummer 

print(mylist[nummer]['voornaam'], mylist[nummer]['achternaam'])
