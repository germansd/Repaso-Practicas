animales=["gato","perro","loro","cocodrilo"]
numeros=[1,2,5,3]
cadena="hola"
for animal in animales:
    print(f"el {animal} es bonito")

for num in numeros:
    result=int(num)*2
    print(result)


#recorrer 2 listas al mismo tiempo
for num,animal in zip(numeros,animales):
    print(num,animal)
#para un rango de numeros
for num in range(5,10):
    print(num)


#recorrer una lista por indice
print("recorrer lista poor indice:")
for num in enumerate(numeros):
    indice=num[0]
    valor=num[1]
    print(f"indice: {indice} valor: {valor}")


#for/else siempre se ejecuta una vez al final
for numero in numeros:
    print(f"ejecutando el ultimo bucle, valor actual:{numero} ")

else:
    print("el blucle termino")


frutas=["banana","pera","manzana","naranja","uvas"]
print("Aqui empieza los bucles con if")
#cuando encuentra en este caso la naranja la omite
for fruta in frutas:
    if fruta=="naranja":
        print(f"encontrada la naranja: {fruta}")
        continue
    print(f"Esta es la fruta: {fruta}")


print("Bucle con break: ")
    #cuando encuentra en este caso la naranja se para el bucle
for fruta in frutas:
    if fruta=="naranja":
        print(f"encontrada la naranja: {fruta}")
        break
    print(f"Esta es la fruta: {fruta}")
print("el bucle termina pq ha encontrafo la naranja")
#para cadenas de texto
for letra in cadena:
    print(letra)


