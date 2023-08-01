"""Escribe una función que verifique si una palabra ingresada por el usuario es un palíndromo.
Un palíndromo es una palabra que se lee igual de izquierda a 
derecha que de derecha a izquierda. Por ejemplo, "radar" y "reconocer" son palíndromos."""
# -*- coding: utf-8 -*-
palindromo = True 
palabra = str(input("Ingresa una palabra:"))

palabra = palabra.replace("","").lower()

for i in range(len(palabra)):
    if palabra[i] != palabra[-(i+1)]:
        palindromo = False
        break
    
if palindromo:
    print("Es palindromo")
else:
    print("No es palindromo")