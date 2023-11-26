# Realiza, utilizando Python 3, un programa llamado binario.py que pida al usuario que
# introduzca un número binario e imprima por pantalla el número en formato decimal.
# Para desarrollar el programa, es necesario que desarrolles una función con la
# siguiente cabecera:
# def esBinario(strbinario)
#   Devuelve True o False si la cadena de caracteres (strbinario) que se ha pasado
# como parámetro contiene una cadena binaria.

def esBinario(strbinario):
    try:
        # Convertir la entrada a cadena
        strbinario = str(strbinario)
        # Comprobación para cada carácter en la cadena
        for digito in strbinario:
            # Si el carácter no es '0' o '1', no es un número binario
            if digito != '0' and digito != '1':
                return False
        return True
    except:
        return False

print(esBinario(1011))

