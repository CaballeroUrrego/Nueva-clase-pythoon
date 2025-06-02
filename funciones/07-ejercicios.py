def no_space(texto):
    nuevo_texto = ""
    for cha in texto:
        if cha != " ":
            nuevo_texto += cha
    return nuevo_texto

def reverse(texto):
    texto_al_reves = ""
    for cha in texto:
        texto_al_reves = cha + texto_al_reves
    return texto_al_reves

def es_palindromo(texto):
    texto = no_space(texto).lower()
    texto_al_reves = reverse(texto)
    return texto.lower() == texto_al_reves.lower()

# Ejemplos de uso:
print("abba", es_palindromo("abba"))
print("Reconocer", es_palindromo("Reconocer"))
print("Amo la paloma", es_palindromo("Amo la paloma"))
print("Hola Mundo", es_palindromo("hola mundo"))