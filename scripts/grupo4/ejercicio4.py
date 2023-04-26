cadena = input("Ingrese una cadena de texto: ")

# Imprimir la longitud de la cadena de texto
print("La longitud de la cadena de texto es:", len(cadena))

# Imprimir la cadena en mayúsculas y en minúsculas
print("Cadena en mayúsculas:", cadena.upper())
print("Cadena en minúsculas:", cadena.lower())

# Buscar una palabra en la cadena de texto e imprimir la cantidad de veces que aparece
palabra = input("Ingrese una palabra para buscar en la cadena de texto: ")
cantidad = cadena.count(palabra)
print("La palabra '", palabra, "' aparece", cantidad,
      "veces en la cadena de texto.")

# Imprimir la cadena de texto invertida
print("Cadena de texto invertida:", cadena[::-1])

# Intercambiar dos palabras en la cadena de texto
palabras = input("Ingrese dos palabras separadas por un espacio: ")
palabra1, palabra2 = palabras.split()
indice1 = cadena.find(palabra1)
indice2 = cadena.find(palabra2)
nueva_cadena = cadena[:indice1] + palabra2 + cadena[
    indice1 + len(palabra1):indice2] + palabra1 + cadena[indice2 +
                                                         len(palabra2):]
print("Cadena de texto con las dos palabras intercambiadas:", nueva_cadena)
