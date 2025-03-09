def saludar(nombreGerman,sexo):
    sexo.lower()
    if sexo=="mujer":
        saludo="reina"
    elif sexo=="hombre":
        saludo="rey"
    else:
        saludo="crak"
    print(f"que tal {nombreGerman} eres mi{saludo}")
    
#nombre=input("introduce tu nombre")
#sexo=input("como te sientes hoy: ")


#saludar(nombre,sexo)





def crear_contrasena(num):
    carac = ["a", "b", "c", "d", "e", "f", "g"]
    num_str = str(num)  # Convertir el número a cadena
    num1 = int(num_str[0])  # Obtener el primer dígito
    c1 = num1 * 2  # Multiplicamos el primer dígito por 2

    c1_c = carac[c1]
    return c1_c,num

    

    
password,numero=crear_contrasena(34)

print(f"tu contraseña es:{password} y el numero que metiste es: {numero}")
