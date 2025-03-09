

def obtener_compañeros(cantidad):
    compañeros=[]
    for i in range(cantidad):
        alumno=input("introduce el nombre de los compañeros")
        edad=int(input("Introduce la edad"))
        compañero=(alumno,edad)
        compañeros.append(compañero)
    compañeros.sort(key=lambda x:x[1])
    asistente=compañeros[0][0]
    profesor=compañeros[-1][0]
    return asistente,profesor
asistente,profesor=obtener_compañeros(3)
print(f"El profesor es {profesor} y el alumno {asistente.upper()}")