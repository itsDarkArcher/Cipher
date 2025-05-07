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
