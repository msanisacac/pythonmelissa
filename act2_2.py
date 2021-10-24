# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 18:23:30 2021

@author: usuario
"""
mayusculas=["K","L","M","N","O","P","Q","R","S","T"]
minusculas=["a","b","c","d","e","f","g","h","i","j"]
caracteres=["%","@","*","$"]
numeros=[0-9]

def validarpassword(password):
    for minusculas in password:
        for mayusculas in password:
            for caracteres in password:
                for numeros in password:
                    if 5<=len(password)<=15:
                        return True
    return False

print("La contraseña que se ingresará a continuación deberá cumplir con los siguientes parámetros:",
      "\nLetras minúsculas entre la a-j",
      "\nLetras mayúsuclas entre la K-T", 
      "\nNúmeros entre 0-9",
      "\nCaracteres especiales(%,$,*,@)",
      "\nEntre los 5 y 15 caracteres")
contraseña=input("Ingrese una contraseña: ")
print(validarpassword(contraseña))

                
                    
            
                
            
            
            
        
        
    
    
    
    