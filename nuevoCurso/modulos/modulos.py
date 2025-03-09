#import modulo_saludar as m_saludar
#se pueden importar las funciones directamente, si se quiere importar variass funciones se pone una coma y se añaden las funciones
from modulo_saludar_hola.modulo_saludar import saludar
saludo=saludar("German")
print(saludo)  

import modulo_saludar_hola.modulo_saludar

saludo2=modulo_saludar_hola.modulo_saludar.saludar("German")
print(saludo2)
