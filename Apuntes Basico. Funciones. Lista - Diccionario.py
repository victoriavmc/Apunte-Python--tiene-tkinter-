# Resolver con practica. No de Sintaxis
# Resolver el problema como se pueda, que funcione, pero cambia el IDE de desarrollo
# El lenguaje le va a dar una magnitud que depende del programador
# -------------------------------------------------------------------------------------------------
# La extension es .py
# Pascal .psc
# -------------------------------------------------------------------------------------------------
# Comentario linea
"""
 Comentario
  Multilinea
  xD
"""
# -------------------------------------------------------------------------------------------------
# Variables
"""
No se especifica de que tipo de variable es.
Declaro un nombre y le asigno un valor.

Igual primero declaramos las variables y después se sigue desarrollando
"""
unNumero = 16  # int
numeroConDecimal = 2.50  # float
unTexto = "Quiero Pepsi."  # str
unBooleano = True  # booleano

mode, lo, de, prueba = "este", 2002, "son", "variables"
tambien = intento = aprobar = 10
# -------------------------------------------------------------------------------------------------
# Importa mucho la identación.
# Usamos Tab
# -------------------------------------------------------------------------------------------------
# Funciones de entrada/salida
print("Print es el escribir. Permite mostrar el texto en consola.")
# -------------------------------------------------------------------------------------------------
# Concatenar
print("Si quiero concatenar usamos:")

print("Donde uso coma. ", mode)

print("Donde uso {} .format para concatenar {}".format(unTexto, lo))

print("Donde uso + para concatenar " + unTexto)
# + No aplica a números, solo texto.

print(
    "Otro es donde se pone f antes comenzar por dentro va en {acaelnombredelavariable} para concatenar ")
print(
    f"Aca para concatenar. {unTexto}.. y ahora voy al quiosco y compro una lata por ${numeroConDecimal}. Re 2002 xD")
# -------------------------------------------------------------------------------------------------
# Para ingresar un valor.
# INPUT le paso un texto que ve el usuario y ahi mismo al responder, se guarda en el valor en el nombre de variable..
# INPUT SIEMPRE RETORNA TEXTO

ejemploDeEntrada = 0
num2prueba = 0
resultado = 0

# se definió el tipo de variable
ejemploDeEntrada = int(
    input("Aca deberá ingresar un ejemplo de variable numérica."))
# aca no se definio que tipo de variable es
num2prueba = input("Aca debe ingresar otro numero")
# aca hago algo con los datos ingresados.
# aca para poder utilizar defino que es un entero
resultado = ejemploDeEntrada+int(num2prueba)
# muestro el resultado
print(f"Resultado con las variables ingresadas son: {resultado}")
# -------------------------------------------------------------------------------------------------
# Funciones para tratar variables. TIPO DE DATOS
"""
Texto a numero INT
Numero a texto STR

Texto str
Numero entero int
Numero real float
Booleano verdadero o falso
"""
# -------------------------------------------------------------------------------------------------
# Condicionales
"""
Condicional Simple

if (condición a cumplir):
    print ("Acciones por el verdadero")
    
Condicional Doble
if (condición a cumplir):
    print ("Acciones por el verdadero")
else:    
    print ("Acciones por el falso")


Condiciones VArias
if (condición a cumplir):
    print ("Acciones por el verdadero");
elif (condición):    
    print ("Acciones por el verdadero de la condición 2. Falso de la primera condición")
else:
    print ("Si no cumple ninguna condición anterior")
"""

print("Ejemplo")
if (resultado == 5):
    print("Igual que 5.")

elif (resultado > 5):
    print("Si es mayor a 5.")

else:
    print("Es menor")
# -------------------------------------------------------------------------------------------------

# Estructuras repetitivas exactas e inexactas. break para salir del bucle.

"""
for combinado con range()
Cuando tengo definido cuantas veces hago.
for "una variable" in range("cantidad de veces o elementos que se repetirá")
empieza del 0. Si quiero un 10 debo poner 11 en range. Hasta el numero anterior del final del bucle.

Range me genera una lista de elementos numéricos 

según los parámetros que le pase a mi rango va a generar de un numero a otro ejemplo
for i in range (2,5)
 print i
 entonces empieza del 2 hasta el 4
 
 si es (4,10,2) devolverá de paso 2 es decir 4,6,8
 
 (0, -10, -2)
 0 , -2, -4, -6 , -8
"""
for i in range(17):
    print(i)
    print("es una variable contadora, que define la cantidad de vueltas")
else:
    print("Fin del bucle.")

# Repetitivas inexactas.
"""
No sabemos y necesitamos una expresión. 
while expresión, identado el contenido del bucle.
while condicionawhile > -1:
"""
# break corta el bucle
# continue vuelve al principio del bucle
# contador += 1 o += Variable
# trabajar con texto entonces todo lo paso a mayuscula o todo a minuscula
# palabra = palabra.upper() Ya mayuscula

ingresa = str(input("Escribi: Pepsi"))
ingresa = ingresa.capitalize()

print(f"Escribi como quieras igual me quedo: {ingresa}")

gato = input("Gatito?")
gato = gato.upper()
print(f"vos decis?... {gato}")

"""
Cuando una accion se repite varias veces. La función ejecuta algo y retorna un valor.
Sino retorna es un procedimiento.

def permite definir la función.
Todo lo que este debajo e identado va a estar dentro de la funcion.

def  nombreDeLaFuncion():
    print("Aca seria una acción que se repite varias veces")    

invoco cuando llamo a la función:

nombreDeLaFuncion()

funcion recursiva es cuando una funcion llama a otra funcion o se invoca a si misma.

def nombredeLaFuncionNumeros (pnum1, pnum2):
    suma= pnum1 + pnum2
    return suma
    
n1 = int input ingrese un número
n2 = int ( input ( "Ingrese un número")
nombredeLaFuncionNumeros(n1,n2)
"""


def nombredeLaFuncionNumeros(pnum1, pnum2):
    suma = pnum1 + pnum2
    print(f"La suma de los números es: {suma}")


def resta(nim1, nim2):
    resta = nim1 - nim2
    return resta


n1 = int(input("Ingrese un numero"))
n2 = int(input("Ingrese un numero:"))
nombredeLaFuncionNumeros(n1, n2)
print("La resta que dio es:", resta(n1, n2))

# SE EXPLICA MEJOR EN EL SIGUIENTE APUNTE. ACA A GRANDES RASGOS
"""
Lista
Listado cantidad de elementos generalmente del mismo tipo.
Se usa cuando tengo un conjunto de elementos y hacer algo... 

Defino una lista ej dia de semanas
cantdiasINDICE=[0,1,2,3,4,5,6]
debemos pedir acceder a traves del indice.

Definir LISTA DE DOS MANERAS
Con palabra reservada

listaSemana = list()

otra manera: 
Se los elementos de la lista, entonces la puedo crear:
listoSemana = ["Lunes","Martes","Miercoles","Jueves","Viernes","Sabado","Domingo"]

COSAS QUE SE PUEDEN HACER CON LA LISTA:

AGREGAR ELEMENTOS A UNA LISTA:
listaSemana.append("agrego esto")

VEO ELEMENTOS DE UNA LISTA:
print(f"Dia {listaSemana[1]}")
entonces me mostraria el dia Martes. Si quiero el primer elemento se pone 0.

SI QUIERO MAS DE 1 ELEMENTO:
print(f"Dia {listaSemana[0:3]}")

MODIFICO UN ELEMENTO:
listaSemana[elemento a modificar] = "este seria el nuevo Valor"
listaSemana[0]= "Tomemos Pepsi asi se va el bajón"

QUIERO BORRAR UN ELEMENTO DE UNA LISTA:
listaSemana.pop()
(SI NO PASO INDICE, BORRA EL ULTIMO ELEMENTO DE LA LISTA.)

SI PEDIS ALGUN ELEMENTO QUE NO ESTA EN LISTA, EJEMPLO MI LISTA SON 3 ELEMENTOS Y PIDO ELEMENTO 7 ENTONCES HABRA ERROR

PARA RECORRER UNA LISTA:
1er metodo
for i in listaSemana:
    print(f"Dia {i}")

2do metodo
un range
for indice in range(len(listaSemana)):
    print(f"Dia {listaSemana[indice]}")

PARA BORRRAR TODA LA LISTA
listaSemana.clear()
"""

"""
DICCIONARIO

persona = dict()
o definir:
persona = {}

es un conjunto de pares, variable y valor
persona= {"nombre": "VictoriaVMC", "cumpleaños":"16/02" , "signo":"Acuario"}

clave y valor.

accedemos a traves de la clave

MODIFICAR UNA CLAVE
persona["cumpleaños"]= "Chusma"

Agregar clave
persona["gaseosaFavorita"]= "Pepsi"

Recorrer diccionario:
for clave,valor in persona.items():
    print(f"Clave {clave}, Valor {valor}")
    
"""
