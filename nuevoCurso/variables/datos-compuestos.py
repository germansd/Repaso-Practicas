#base 0
#esto es una lista(Matriz)
lista=["German Sanchez","Soy German",True,1.85]
#la tupla no se puede modificar
tupla=("German Sanchez","Soy German",True,1.85)

print(lista[1])
print(tupla[1])



#crear un conjunto (set) (no accede a elementos por indice,no almacena datos repetidos, pone todo en desorden)
conjunto={"German sanchez","Soy german",1.85,"Soy german"}
print(conjunto)

#diccionario (dict)
#clave valor
diccionario={
    'nombre':"German",
    'esta_emocionado':True,
    'edad':1.85
}
#devuelve verdadero
print("German"in diccionario["nombre"])
