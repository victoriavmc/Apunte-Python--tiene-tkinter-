import random
#RANDINT ES N ALEATORIO ENTRE UN numero y otro.
comienza = random.randint(0, 1)
if comienza == 0:
    print('Comienza el jugador')
else:
    print('Comienza el PC')

#CHOICE devuelve un elemento aleatorio de una secuencia. Es muy útil cuando hay que elegir al azar un elemento de entre un conjunto.
frutas = ['peras', 'manzanas', 'plátanos', 'ciruelas']
for i in range(3):
    print(random.choice(frutas))

#Shuffle(lista) modifica el orden de los elementos de una lista.
baraja = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
print(baraja)
for i in range(3):
    random.shuffle(baraja)
print(baraja)

#Sample(lista, cantidad). Esta función devuelve num elementos aleatorios de la secuencia sec.
barajaNueva = [1, 2, 3, 4, 5, 6, 7, 10, 11, 12]
print(random.sample(barajaNueva, 5))