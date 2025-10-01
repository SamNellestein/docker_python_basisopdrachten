# Opdracht 3 input functie
# Naam student:
# Groep:

# Hier komt je code...

# Hier start de for-loop

pizzas = 'margharita', 'funghi', 'quattro stagioni', 'quattro formaggi', 'tonno', 'calzone'
print("startlijst:", pizzas)

pizzas.sort()
print("gesorteerde lijst:", pizzas)

pizzas.append('yo-favorito')
print("met extra pizza:", pizzas)

pizzas.remove('funghi')
print("zonder funghi:", pizzas)

print ("eerste pizza:", pizzas[:3])

print ("middelste pizza:", [pizzas[len(pizzas)//2]])

print("laatste 3 pizzas:", pizzas[-3:])