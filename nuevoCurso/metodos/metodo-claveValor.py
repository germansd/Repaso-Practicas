diccionario={
    "nombre": "German",
    "apellido": "sanchez",
    "edad": 25
}
#te dice las claves del diccionario
claves=diccionario.keys()
print(claves)
#preguntar la clave y te da el valor
clave=diccionario.get("nombre")
print(clave)


#eliminar una clave
diccionario.pop("edad")
print(diccionario)