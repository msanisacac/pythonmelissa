# -*- coding: utf-8 -*-
"""

@author: usuario
"""
print(input("Realizado por: "))

variable1=875
print(type(875))
#Las funciones print y type sirvieron como medios para reconocer el tipo de dato mostrado
#El tipo de dato es un entero <int>

variable2=4.89
print(type(4.89))
#El tipo de dato es un decimal; por tanto el intérprete lo reconocerá como <float>

variable3="Now is better than never"
print(type("Now is better than never"))
#El tipo de dato es un frase; por tanto el intérprete lo reconocerá como <str>

variable4=1.32
print(type(1.32))
#El tipo de dato es un decimal; por tanto el intérprete lo reconocerá como <float>

variable5=5+8j
print(isinstance(5+8j,int))
#La función isinstance arroja valores lógicos: True or False, dependiendo de si el dato ingresado clasifica dentro del grupo indicado

variable6=8.2
print(isinstance(8.2,int))
#La función isinstance identificará si el dato ingresado <8.2> es o no clasificado como <int>

variable7="Readability counts"
print(isinstance("Readability counts",str))
#La función isinstance reconocerá si la frase clasifica o no dentro de <str>