cadena1="german sanchez"
cadena2="SANCHEZ GERMAN"

mayuscula=cadena1.upper()

print(mayuscula)

minuscula=cadena2.lower()
print(minuscula)

#primera letra en mayuscula
primera_letra=cadena1.capitalize()
print(primera_letra)

#buscamos una cadena en otra(base 0),si no encuentra devuelve -1
busqueda=cadena1.find("z")
print(busqueda)


#funcion para saber si es numerico
numerico=cadena1.isnumeric()
print(numerico)

#contar coincidencias
coincidencias=cadena1.count("man")
print(coincidencias)

#contamos los caracteres de la cadena
contar_caracteres=len(cadena1)
print(contar_caracteres)

#verificamos si una cadena empieza con una cadena
empieza_con=cadena1.startswith("g")
print(empieza_con)

#verificamos si una cadena termina con una cadena
termina_con=cadena1.endswith("chez")
print(termina_con)

#reemplaza un valor
reemplazo=cadena1.replace("german","juan")
print(reemplazo)

#separa cadenas con el caracter dado, devuelve una lista
separar=cadena1.split(" ")
print(separar[0])