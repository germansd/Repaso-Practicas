def suma(nombre,*numeros):
    return f"{nombre}, la suma de tus nuneros es:{sum(numeros)}"

resultado=suma("Germán",5,3,9,10,20)
print(resultado)