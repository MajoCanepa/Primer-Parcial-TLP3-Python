# #Se está trabajando en un programa que necesita capitalizar palabras, pero el desafío es
# que solo la primera letra debe ser convertida a mayúscula, manteniendo las demás
# letras sin cambios.

# Especificaciones de la Función:
# Nombre de la función:
# ● El nombre de la función debe ser: capitalizar_palabra
# Parámetros:
# ● palabra (str): Una cadena de caracteres que representa la palabra a
# capitalizar.

# Retorno:
# ● str: La palabra capitalizada con la primera letra en mayúscula y las demás
# letras sin cambios.
def capitalizar_palabra(palabra: str):
    return palabra.capitalize()

palabra = 'ciencia de datos'
resultado = capitalizar_palabra(palabra)
print(palabra.capitalize())



