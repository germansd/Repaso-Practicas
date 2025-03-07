uno=1
dos=2
uno="1"
try:
    print(uno+dos)
    print("no se han producido excepciones")

except TypeError as error:
    print(f"Se ha producido una excepción: {error}")



else:
    #se ejecuta si no hay excepcion
    print("la ejecucion contunua correctamente")

finally:
    #se ejecuta siempre
    print("continua")