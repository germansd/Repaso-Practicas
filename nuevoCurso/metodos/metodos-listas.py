lista1=["hola","german",1.85,True]
#cantidad de elementos
print(len(lista1))
#agregar elemento
lista1.append("Sanchez")
print(lista1)

#agregar con posiciones
lista1.insert(1,"Garcia")
print(lista1)

#agregar varios elementos a la lista
lista1.extend([False,200])
print(lista1)


#elimina un elemento de la lista por su indice

lista1.pop(0)
print(lista1)

#eliminando por su valor
lista1.remove("Garcia")
print(lista1)

#ordenar
#lista1.sort()

#ordenar al reves
#lista1.sort(reverse=True)

#verificar si un elemento se encuentra en una lista
encontrado=lista1.index("Sanchez")
print(encontrado)
