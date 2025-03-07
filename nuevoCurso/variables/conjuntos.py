conjunto=set(["Dato 1","Dato 2"])
print(conjunto)

conjunto1=frozenset(["dato1,","dato2"])
conjunto2={conjunto1,"Dato3"}
print(conjunto2)

#teoria de conjuntos

conjunto1={
    1,3,5,7
}
conjunto2={
    1,3,7
}
#es un subcojunto?
resultado=conjunto2.issubset(conjunto1)
print(resultado)

#es un superconjunto?
resultado=conjunto1.issuperset(conjunto2)
print(resultado)

#verificar si hay algun numero en comun
#si algun numero esta en los conjuntos devuelve false
resultado=conjunto2.isdisjoint(conjunto1)
print(resultado)