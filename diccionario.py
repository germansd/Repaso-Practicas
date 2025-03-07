diccionario={
    "Nombre":"German",
    "Apellido":"Sanchez",
    "Edad":18,
    "Ciudad":{"Madrid","Cazalegas"}
}
print(diccionario)
print(len(diccionario))#para contar
diccionario["Nombre"]="Alfredo"
print(diccionario["Nombre"])#para acceder a un valor


del diccionario["Nombre"] #eliminar
print(diccionario)
#operadores de pertenencia
#comprobar si una palabra esta
print("Apellido" in diccionario)


print(diccionario.keys())#saca las claves

print(diccionario.items())#saca la clave y el valor

print(diccionario.fromkeys(diccionario,"Sanchez"))#saca de cada clave el valor es sanchez

print(diccionario.values())#solo saca los valores sin las claves




