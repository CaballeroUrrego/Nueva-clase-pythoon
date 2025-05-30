def es_palindromo(texto):
    # Eliminar espacios y convertir a minúsculas
    texto_limpio = ''.join(texto.lower().split())
    # Comprobar si es igual al revés
    return texto_limpio == texto_limpio[::-1]

# Pruebas
print("abba", es_palindromo("abba"))
print("Reconocer", es_palindromo("Reconocer"))
print("Amo la paloma", es_palindromo("Amo la paloma"))
print("Hola Mundo", es_palindromo("hola mundo"))