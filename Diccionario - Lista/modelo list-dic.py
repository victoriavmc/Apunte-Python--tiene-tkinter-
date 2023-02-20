#Diccionario
Diccionario = {}
DiccionarioPreestablecido = {"Csgo":"Jugamo?", "Pepsi":16}
#len cuenta cantidad elementos
print("""\n -·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·- \n""")
print(len(DiccionarioPreestablecido))
#Agregar cosas al diccionario.
print("""\n -·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·- \n""")
Diccionario["NUEVA CLAVE"]="EL VALOR NUEVO"
print(Diccionario)
print("""\n -·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·- \n""")
#Buscar una clave:
for clave in DiccionarioPreestablecido.keys():
    #Aca recorre todas las claves, si quiero una en especifica dentro del for:
    if clave == "Csgo":
        #Solo imprimira la clave que quiero
        print(f"Si existe la clave: {clave}, en el diccionario")
print("""\n -·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·- \n""")
#Buscar un valor:
for valor in DiccionarioPreestablecido.values():
    #Aca recorre todas los valores, si quiero una en especifica dentro del for:
    if valor == 16:
        #Solo imprimira el valor que quiero
        print(f"Si existe el valor: {valor}, en el diccionario")
print("""\n -·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·- \n""")
#Ocupare los dos datos:
for clave, valor in DiccionarioPreestablecido.items():
    #Aca recorre todas las claves y sus respectivos valores.
    print(f"La clave: {clave}. Tiene el valor: {valor}")
    #segun el valor que tenga muestra un mensaje
    if valor !=16:
        print("No la contesss...")
    else:
        print("Mortal")
print("""\n -·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·- \n""")
#Una manera de asegurar si existe y despues armar algo es:
print("Aca muestro el diccionario que elementos tiene.", DiccionarioPreestablecido)
veoExiste = "Existo?"
existe = veoExiste in DiccionarioPreestablecido.keys()
if existe:
    for clave, valor in DiccionarioPreestablecido.items():
        print(f"La clave: {clave}. Tiene el valor: {valor}")
else:
    print(f"... Amigo... La clave {veoExiste}.... NOOOOOO!... Decile a mamá que... quiero una pepsi, Gracias.")
print("""\n ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ \n""")
#OTRA MANERA
veoExiste2 = "Csgo"
print("Aca mostrara el valor que tiene esa clave:")
print(DiccionarioPreestablecido.get((veoExiste2),f"No existe la clave {veoExiste2} en el diccionario")) 
print("""\n ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ \n""")
#OTRA MANERA MAS
variable = 16
if variable in DiccionarioPreestablecido:
    print(f"Existe la clave {variable} en el diccionario")
else:
    print(f"No existe la clave {variable} en el diccionario")
print("""\n -·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·- \n""")
#Crear un diccionario con listas:
listaClaves=[10,"Nunca Puede Faltar","Indice"]
listaValores=["Messirve xd", 16, "Contenido"]
diccionarioCreadoLista = dict(zip(listaClaves,listaValores))
print(diccionarioCreadoLista)
#borrar todo el diccionario
diccionarioCreadoLista.clear()
print("""\n ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ \n""")
#Otra manera de hacer
for unaClave, unValor in zip(listaClaves, listaValores):
    diccionarioCreadoLista[unaClave] = [unValor]
print (diccionarioCreadoLista)
diccionarioCreadoLista.clear()
print("""\n ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ \n""")
#OtraManera si es con funcion:
# def fDiccio(claves, valores):
#     diccio = {}
#     for letra in range(len(clav)):
#         diccio[claves[i]]=valores[i]
#     return diccio

# Listaclave = ['diez', 'veinte', 'treinta']
# Listavalor = [10, 20, 30]
# diccionario = fDiccio(Listaclave,Listavalor)
# print(diccionario)
print("""Comentado la funcion jejox \n""")
#Diccionario con Lista adentro
DiccionarioModelo = {"AcaModelo":[2, 16, "Pepsi"], 52 :[30, 100, "Coca-Cola"] }
for clave, listaElementos in DiccionarioModelo.items():
    #La clave es la key del diccionario
    #listaElementos es una lista
    print("""^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n""")
    print(listaElementos)
    print("""\n ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ \n""")
    print("Diccionario que existe:" , DiccionarioModelo)
    sumar = listaElementos[0] + listaElementos[1]
    print(f"De la clave: {clave}, la suma de sus primeros dos elementos {sumar}")
    print("""\n ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ \n""")
    for elementos in listaElementos:
        #aca imprime cada elemento de la lista
        print(elementos ,"\n")
print("""\n ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ \n""")
#Diccionario con Lista adentro
DiccionarioModelo = {"AcaModelo":[2, 16, "Pepsi"], 52 :[10, 80, "Coca-Cola"] }
for clave, listaElementos in DiccionarioModelo.items():
    #listaElementos es una lista
    if listaElementos[0]> 2:
        print(f"Compraste muchas {listaElementos[2]}. Cantidad: {listaElementos[0]}. Gastaste: ${listaElementos[1]}")
    else:
        print(f"Compra mas {listaElementos[2]}. Solo compraste: {listaElementos[0]}. Rata igual gastaste: ${listaElementos[1]}")
print("""\n -·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·- \n""")
#Diccionario con Dicionario
diccionariosxD = {"NombredePersona":{"edad":16, "sexo":"F", "sueldo":100}, "NombrePersona2":{"edad":20, "sexo":"M", "sueldo":400}}
for clave, valor in diccionariosxD.items():
    if clave == "NombredePersona":
        print(valor["edad"])
print("""\n -·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·- \n""")
for clave, diccionario2 in diccionariosxD.items():
    for clave2, valor in diccionario2.items():
        print(valor)
        #Agora sim
print("""\n-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-""")
print("""-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-""")
print("""-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-""")
#Lista
#Lista toma [ 0, 1, 2 ....] simpre del 0 parte.
Lista = []
ListaQonda = ["A" , "B", 16]
print("""-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·- \n""")
print("Mi lista:", ListaQonda)
ListaQonda.append("Toma agua uwu")
print("Misma lista pero agrege algo ^u^:", ListaQonda)
print("""\n -·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·- \n""")
ListaAmego = [16, 2, 1]
print(ListaAmego)
for elemento in (ListaAmego):
    if 2 < elemento :
        print("Es mayor a 2.")
    elif elemento  ==2:
        print("E lo mimo")
    else:
        print("Menor")
print("""\n -·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·- \n""") 
correoVerifica = ["VictoriaVMC@gmail.com", "no"]
for elementos in (correoVerifica):
    print(elementos)
    caracterEspecial = False
    for letra in elementos:
        if letra == "@":
            caracterEspecial= True
    if caracterEspecial == True:
        print("Ingreso su correo con exito!.")
    else:
        print("Falto el '@' del correo electronico...")
print("""\n -·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·- \n""")
listaultimo = [16, 2, 2002]
print("La lista:", listaultimo)
print(f"Tiene: {len(listaultimo)} elementos")
print("""\n -·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·-·- \n""")