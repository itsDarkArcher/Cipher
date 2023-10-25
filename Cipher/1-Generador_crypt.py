import random
import string
import pickle
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

def separar_palabras(nombre_heroe):
    palabras = []
    palabra_actual = ""
    for letra in nombre_heroe:
        if letra.isupper():
            if palabra_actual:
                palabras.append(palabra_actual)
            palabra_actual = letra
        else:
            palabra_actual += letra
    if palabra_actual:
        palabras.append(palabra_actual)
    return ' '.join(palabras)

def generar_contraseña():
    heroes = []#insert your own list of words
    heroe = random.choice(heroes).replace(" ", "")
    numero = random.randint(0, 99)
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(13))
    contraseña = ''.join(caracter for caracter in contraseña if caracter not in heroe)
    
    key = RSA.generate(2048)
    
    cipher = PKCS1_OAEP.new(key)
    contraseña_encriptada = cipher.encrypt(contraseña.encode())
    
    cifrado = {
        "heroe": heroe,
        "numero": numero,
        "contraseña": contraseña_encriptada,
        "private_key": key.export_key()
    }

    try:
        with open('KeyWords.pkl', 'rb') as archivo:
            contraseñas = pickle.load(archivo)
    except FileNotFoundError:
        contraseñas = []

    contraseñas.append(cifrado)

    with open('KeyWords.pkl', 'wb') as archivo:
        pickle.dump(contraseñas, archivo)
    
    return heroe, numero, contraseña_encriptada

heroe, numero, contraseña_encriptada = generar_contraseña()
nombre_heroe_separado = separar_palabras(heroe)

print(f"Se ha generado una contraseña cifrada para el héroe {nombre_heroe_separado} con el número {numero}.")
