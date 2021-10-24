# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 17:58:21 2021

@author: usuario
"""

Datos_2021 = [1,2,3,4,5,6,7,100,91,110,900,21,33,32,2,4,8,10,13,13,16,15,1302]
numero_par=[2,4,6,100,110,900,32,2,4,8,10,16,1302]
numero_impar=[1,3,5,7,91,21,33,13,13,15]

def par_impar(numero):
    if numero%2==0:
        numero_par.append(numero)
    elif numero%2!=0:
        numero_impar.append(numero)

print("La cadena original es:",Datos_2021,"\n")
for num in Datos_2021:
    par_impar(num)
print("Numeros pares",numero_par)
print("Numeros impares",numero_impar)
        

    



