import pickle
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
#extraemos los datos del archivo .plk previamente creado donde se almacenan las contraseñas y sus llaves
def cargar_datos(heroe, numero):
    try:
        with open('KeyWords.pkl', 'rb') as archivo:
            contraseñas = pickle.load(archivo)
            for cifrado in contraseñas:
                if cifrado['heroe'] == heroe and cifrado['numero'] == numero:
                    return cifrado
            return None
    except FileNotFoundError:
        print("El archivo 'KeyWords.pkl' no se encuentra. Por favor, asegúrate de haber generado una contraseña primero.")
        return None
    except (EOFError, KeyError):
        print("No se encontraron datos válidos en el archivo 'KeyWords.pkl'.")
        print("Genera una contraseña primero.")
        return None
#extraemos el key de cifrado
def cargar_private_key():
    try:
        with open('private_key.pem', 'rb') as archivo:
            pem = archivo.read()
            private_key = RSA.import_key(pem)
        return private_key
    except FileNotFoundError:
        print("El archivo 'private_key.pem' no se encuentra. Por favor, asegúrate de haber generado una contraseña primero.")
        return None
#desencripta la contraseña solicitada con su respectiva llave
def desencriptar_contraseña(heroe, numero):
    cifrado = cargar_datos(heroe, numero)
    if cifrado is not None:
        private_key = RSA.import_key(cifrado['private_key'])
        cipher = PKCS1_OAEP.new(private_key)
        contraseña = cipher.decrypt(cifrado['contraseña'])
        return contraseña.decode()

#Solicita que ingrese la palabra y numero utilizados para crear la contraseña que queremos desencriptar 
heroe = input("Ingresa el héroe: ").replace(" ", "")
numero = int(input("Ingresa el número: "))

# Modo de uso
contraseña = desencriptar_contraseña(heroe, numero)
if contraseña is not None:
    print(f"La contraseña generada es: {contraseña}")
else:
    print("No se pudo desencriptar la contraseña.")
