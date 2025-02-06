# Cipher
#### Video Demo: [Watch Here](https://youtu.be/LrJnulqus_M)

## Overview
Cipher es un generador y gestor de contraseñas que proporciona funcionalidad básica para la encriptación, desencriptación y generación de contraseñas utilizando encriptación RSA. Utiliza una lista de superhéroes y números aleatorios como parte de las claves de encriptación, asegurando una mayor seguridad.

## Libraries Used
- **random**: Genera valores aleatorios.
- **pickle**: Serializa y deserializa objetos de Python.
- **string**: Ofrece operaciones comunes de cadenas.
- **Crypto.PublicKey.RSA**: Proporciona funciones de encriptación y desencriptación RSA.
- **Crypto.Cipher.PKCS1_OAEP**: Implementa el Padding de Encriptación Asimétrica Óptima (OAEP) de RSA.
- **os**: Interactúa con el sistema operativo.
- **sys**: Manipula diferentes partes del entorno de ejecución de Python.

## Global Variables
- **heroes**: Una lista de nombres de superhéroes utilizada para la encriptación de contraseñas.

## Functions
1. **main()**: Ejecuta el programa y presenta opciones de menú al usuario.
2. **generate_password()**: Genera una contraseña aleatoria de longitud 18 con guiones y puntos.
3. **encrypt_password(password)**: Encripta una contraseña dada utilizando encriptación RSA.
4. **decrypt_password()**: Desencripta una contraseña basada en la entrada del usuario.
5. **load_data(hero, number)**: Carga datos del archivo de contraseñas guardadas.
6. **decrypt(cipher_data)**: Desencripta la contraseña utilizando la clave privada asociada.
7. **encrypt_user_password()**: Solicita al usuario que ingrese una contraseña y la encripta.
8. **generate_encrypted_password()**: Genera y encripta una contraseña aleatoria.

## Execution Flow
- El script comienza importando las bibliotecas necesarias y definiendo variables globales.
- Define varias funciones para generar, encriptar y desencriptar contraseñas, y manejar la entrada del usuario.
- La función **main()** sirve como punto de entrada, presentando un menú al usuario y manejando su entrada.
- Dependiendo de la elección del usuario, se llaman las funciones correspondientes para realizar la encriptación, desencriptación, generación de contraseñas o salir del programa.
- Se implementa el manejo de errores para gestionar la entrada inesperada o excepciones de manera adecuada.

## Password Generation
- La función **generate_password()** crea una contraseña fuerte de longitud 18 con guiones y puntos colocados aleatoriamente.

## Password Encryption
- La función **encrypt_password(password)** encripta una contraseña usando encriptación RSA, asociándola con un nombre de superhéroe y un número seleccionados aleatoriamente.
- Las contraseñas encriptadas y los datos asociados se almacenan en un diccionario para su recuperación.

## Password Decryption
- La función **decrypt_password()** solicita al usuario un héroe y un número, busca en el archivo de contraseñas guardadas, y desencripta la contraseña si se encuentra.

## File Handling
- El script utiliza el módulo **pickle** para guardar y cargar datos de contraseñas encriptadas desde un archivo llamado 'Encrypt.pkl'.
- El manejo de errores asegura que el programa gestione escenarios como archivo no encontrado o datos inválidos.

## User Interaction
- El script proporciona una interfaz amigable con un menú de opciones y maneja la entrada del usuario mediante funciones **input()**.
- El manejo de excepciones captura errores y proporciona mensajes informativos al usuario.

## Code Organization
- Las funciones están organizadas para mejorar la legibilidad y mantenibilidad.
- Se proporcionan comentarios para explicar el propósito de cada función y bloques de código significativos.

## Error Handling
- El script utiliza bloques **try-except** para manejar excepciones de manera adecuada, evitando fallos.
- La función **main()** captura excepciones **KeyboardInterrupt** para manejar interrupciones del usuario de manera limpia.
- Un manejador genérico de **Exception** captura y muestra cualquier error inesperado.

## Randomness and Security
- Se introduce aleatoriedad en la generación de contraseñas, selección de superhéroes y generación de pares de claves RSA para mejorar la seguridad y asegurar la imprevisibilidad.
