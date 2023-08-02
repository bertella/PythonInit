print('Ingresa la palabra:')
palabra = input()

contador_vocales = 0
contador_consonantes = 0

vocales = 'aeiou'

for caracter in palabra:
    if caracter.isalpha():  # Verificamos si el caracter es una letra
        if caracter in vocales:
            contador_vocales += 1
        else:
            contador_consonantes += 1

print("Cantidad de vocales:", contador_vocales)
print("Cantidad de consonantes:", contador_consonantes)