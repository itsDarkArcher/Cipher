# Cipher
#### Video Demo:  <https://youtu.be/LrJnulqus_M>

## Overview

Cipher is a Python project that provides functionality for password encryption, decryption, and generation using RSA encryption. The project includes a command-line interface and a Flask-based web API.

## Libraries Used

- **`random`**: Used for generating random values.
- **`string`**: Provides a collection of common string operations.
- **`Crypto.PublicKey.RSA`**: Provides functions for RSA encryption and decryption.
- **`Crypto.Cipher.PKCS1_OAEP`**: Provides functions for implementing the RSA's Optimal Asymmetric Encryption Padding (OAEP).
- **`sqlite3`**: Provides functions for interacting with SQLite databases.
- **`Flask`**: A micro web framework for Python.
- **`flask-cors`**: A Flask extension for handling Cross-Origin Resource Sharing (CORS).

## Global Variables

- **`heroes`**: A list of superhero names used for password encryption.

## Functions in `project.py`

1. **`main()`**: The main function that executes the program. It presents a menu of options to the user and calls corresponding functions based on the user's choice.
2. **`generate_password()`**: Generates a random password of length 18 with randomly placed hyphens and periods.
3. **`encrypt_password(password)`**: Encrypts a given password using RSA encryption. It selects a random hero and number, generates an RSA key pair, and stores the encrypted password along with associated data.
4. **`decrypt_password()`**: Decrypts a password. It prompts the user to enter a hero and a number, searches for matching data in the database, and decrypts the password if found.
5. **`decrypt(cipher_data)`**: Decrypts the password using the private key associated with the encrypted password.
6. **`encrypt_user_password()`**: Prompts the user to enter a password and encrypts it using the `encrypt_password()` function. Checks if the password meets the strength criteria.
7. **`generate_encrypted_password()`**: Generates a random password using `generate_password()` and encrypts it using the `encrypt_password()` function.
8. **`check_password_strength(password)`**: Checks if the password meets the strength criteria (at least 12 characters, with at least 1 uppercase, 1 lowercase, a digit, and a special character).
9. **`load_data(hero, number)`**: Loads data from the database and searches for matching hero and number.
10. **`setup_database()`**: Sets up the database if it doesn't exist.

## Functions in `backend_flask/app.py`

1. **`generate_password()`**: Endpoint to generate a random password with hyphens and periods randomly placed.
2. **`encrypt_password()`**: Endpoint to encrypt a given password.
3. **`decrypt_password()`**: Endpoint to decrypt a password.
4. **`decrypt(cipher_data)`**: Decrypts the password using the private key.
5. **`load_data(hero, number)`**: Loads data from the database and searches for matching hero and number.
6. **`setup_database()`**: Sets up the database if it doesn't exist.

## Password Handling and Storage

Passwords are encrypted using RSA encryption and stored in an SQLite database. Each password is associated with a randomly selected superhero name and a number. The encrypted passwords, along with the associated data, are stored in the database for later retrieval and decryption.

## Tests

The project includes unit tests in the `tests/test_project.py` file to ensure the functionality of the password encryption and decryption processes.

### Running Tests

To run the tests, use the following command:

```sh
python -m unittest discover -s tests
```
## Setup and Installation

1. Clone the repository:
    ```sh
    git clone <repository-url>
    ```
2. Navigate to the project directory:
    ```sh
    cd Cipher
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4. Run the Flask application:
    ```sh
    python backend_flask/app.py
    ```

## Usage

### Command-Line Interface

Run the [project.py](http://_vscodecontentref_/1) script to start the command-line interface:

```sh
python project.py
```

You will be presented with the following menu options:

1. **Encrypt User Password**: Prompts the user to enter a password and encrypts it.
2. **Generate Encrypted Password**: Generates a random password and encrypts it.
3. **Decrypt Password**: Prompts the user to enter a hero and a number, and decrypts the corresponding password.
4. **Exit**: Exits the program.

### Web API

The Flask application provides the following endpoints:

- **`GET /generate_password`**: Generates a random password.
- **`POST /encrypt_password`**: Encrypts a given password.
- **`POST /decrypt_password`**: Decrypts a password.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
=======
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
