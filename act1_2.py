# -*- coding: utf-8 -*-
"""


@author: usuario
"""
variable1=int(input("Ingrese un dato cualquiera:"))
print("Este tipo de dato en python es:")
try:
    type(variable1)
except ValueError:
    print("El dato ingresado no es un entero")
else:
    print(type(variable1))
    print("El dato ingresado es un entero")


variable2=float(input("Ingrese un dato cualquiera:"))
print("Este tipo de dato en python es:")
try:
    type(variable2)
except ValueError:
    print("El dato ingresado no es un decimal")
else:
    print(type(variable2)) 
    print("El dato ingresado es un decimal")
    

variable3=str(input("Ingrese un dato cualquiera:"))
print("Este tipo de dato en python es:")
try:
    type(variable3)
except ValueError:
    print("El dato ingresado no es un string")
else:
    print(type(variable3))
    print("El dato ingresado es un string")


variable4=complex(input("Ingrese un dato cualquiera:"))
print("Este tipo de dato en python es:")
try:
    type(variable4)
except ValueError:
    print("El dato ingresado no es un número complejo")
else:
    print(type(variable4))
    print("El dato ingresado es un numero complejo")

    
variable5=int(input("Ingrese un dato cualquiera:"))
print("Este tipo de dato en python es:")
try:
    type(variable5)
except ValueError:
    print("El dato ingresado no es un entero")
else:
    print(type(variable5))
    print("El dato ingresado es un entero")