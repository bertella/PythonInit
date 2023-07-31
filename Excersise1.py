
# -*- coding: utf-8 -*-
import random

numero_secreto = random.randint (1,10)
intentos =  0 

print("Bienvenidos a ...::: ADIVINA EL NUMERO ::... ")
print("Estoy pensando en un numero entre 1 y 100 podes adivinar cual es ?... ")

while True:
    intento = int(input('Introduce el numero'))
    intentos += 1 
    
    if intento < numero_secreto:
        print(" El Numero es mas Grande ")
    elif intento > numero_secreto:        
        print("El numero es mas chico")
    else:
        print("Felicitaciones Adivinaste el Numero en {intentos} intentos "    )
        break   
  
