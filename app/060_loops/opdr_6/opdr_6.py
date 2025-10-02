# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Hier start de for-loop

pizzas = ('calzone', 'margharita', 'olivio', 'quattro stagioni', 'verdi', 'yo-favorito')
print("startlijst:", pizzas)

pizzas = sorted(pizzas)
print("gesorteerde lijst:", pizzas)

pizzas.append('yo-favorito')
print("met extra pizza:", pizzas)

pizzas.remove('verdi')
print("zonder verdi:", pizzas)

print ("eerste pizza:", pizzas[:3])

print ("middelste pizza:", [pizzas[len(pizzas)//2]])

print("laatste 3 pizzas:", pizzas[-3:])