print("=== CIFRADO CÉSAR ===")

mensaje = input("Escribe el mensaje: ")
desplazamiento = int(input("Escribe el desplazamiento: "))

alfabeto = "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMÑOPQRSTUVWXYZ"
mensaje_cifrado = ""
mensaje_descifrado = ""
#parte inicial del programa

# CIFRADO
for caracter in mensaje:
    if caracter in alfabeto:
        posicion = alfabeto.index(caracter)
        nueva_posicion = (posicion + desplazamiento) % len(alfabeto)
        mensaje_cifrado += alfabeto[nueva_posicion]
    else:
        mensaje_cifrado += caracter

print("\nMensaje cifrado:", mensaje_cifrado)

# DESCIFRADO
for caracter in mensaje_cifrado:
    if caracter in alfabeto:
        posicion = alfabeto.index(caracter)
        nueva_posicion = (posicion - desplazamiento) % len(alfabeto)
        mensaje_descifrado += alfabeto[nueva_posicion]
    else:
        mensaje_descifrado += caracter
        #parte final del programa

print("Mensaje descifrado:", mensaje_descifrado)
