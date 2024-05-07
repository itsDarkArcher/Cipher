# Cipher
    #### Video Demo:  <https://youtu.be/LrJnulqus_M>
    #### Description:

### Libraries Used:

- **`random`**: Used for generating random values.
- **`pickle`**: Used for serializing and deserializing Python objects.
- **`string`**: Provides a collection of common string operations.
- **`Crypto.PublicKey.RSA`**: Provides functions for RSA encryption and decryption.
- **`Crypto.Cipher.PKCS1_OAEP`**: Provides functions for implementing the RSA's Optimal Asymmetric Encryption Padding (OAEP).
- **`os`**: Provides functions for interacting with the operating system.
- **`sys`**: Provides functions and variables used to manipulate different parts of the Python runtime environment.

### Global Variables:

- **`heroes`**: A list of superhero names used for password encryption.

### Functions:

1. **`main()`**: The main function that executes the program. It presents a menu of options to the user and calls corresponding functions based on the user's choice.
2. **`generate_password()`**: Generates a random password of length 18 with randomly placed hyphens and periods.
3. **`encrypt_password(password)`**: Encrypts a given password using RSA encryption. It selects a random hero and number, generates an RSA key pair, and stores the encrypted password along with associated data.
4. **`decrypt_password()`**: Decrypts a password. It prompts the user to enter a hero and a number, searches for matching data in the saved passwords file, and decrypts the password if found.
5. **`load_data(hero, number)`**: Loads data from the saved passwords file and searches for matching hero and number.
6. **`decrypt(cipher_data)`**: Decrypts the password using the private key associated with the encrypted password.
7. **`encrypt_user_password()`**: Prompts the user to enter a password and encrypts it using the **`encrypt_password()`** function. Checks if the password is at least 12 characters long.
8. **`generate_encrypted_password()`**: Generates a random password using **`generate_password()`** and encrypts it using the **`encrypt_password()`** function.

### Execution:

- The script starts by calling the **`main()`** function.
- The user is presented with a menu of options: encrypt user password, generate encrypted password, decrypt password, and exit.
- Depending on the user's choice, corresponding functions are called to perform the desired operation.
- The script handles errors gracefully and provides appropriate error messages.

This script provides basic functionality for password encryption, decryption, and generation, using RSA encryption with randomly selected heroes and numbers for encryption keys. It's a simple example of encryption techniques and user interaction in Python.

### Execution Flow:

- The script starts by importing necessary libraries and defining global variables.
- It then defines several functions for various tasks such as generating passwords, encrypting passwords, decrypting passwords, and handling user input.
- The **`main()`** function is the entry point of the script. It presents a menu to the user and handles their input.
- Depending on the user's choice, the script calls corresponding functions to perform encryption, decryption, password generation, or exiting the program.
- Error handling is implemented throughout the script to gracefully handle unexpected input or exceptions.

### Password Generation:

- The **`generate_password()`** function generates a random password of length 18 with randomly placed hyphens and periods. It combines letters and digits to create a strong password.

### Password Encryption:

- The **`encrypt_password(password)`** function encrypts a given password using RSA encryption. It selects a random hero and number from the **`heroes`** list, generates an RSA key pair, and stores the encrypted password along with associated data in a dictionary.

### Password Decryption:

- The **`decrypt_password()`** function prompts the user to enter a hero and a number. It then searches for matching data in the saved passwords file and decrypts the password if found using the associated private key.

### File Handling:

- The script uses the **`pickle`** module to serialize and deserialize Python objects, allowing it to save and load encrypted password data to and from a file named 'Encrypt.pkl'.
- Error handling is implemented to handle scenarios such as file not found or invalid data in the file.

### User Interaction:

- The script provides a user-friendly interface by presenting a menu of options and handling user input using **`input()`** functions.
- It uses exception handling to catch errors and provide informative error messages to the user.

### Code Organization:

- The code is well-organized into functions, each serving a specific purpose, which improves readability and maintainability.
- Comments are provided throughout the code to explain the purpose of each function and significant code blocks.

### Error Handling:

- The script implements error handling using **`try-except`** blocks to catch and handle exceptions gracefully. This ensures that the program doesn't crash when unexpected errors occur.
- In the **`main()`** function, it catches **`KeyboardInterrupt`** exceptions to handle interruptions caused by the user pressing Ctrl+C, allowing the program to exit cleanly.
- Additionally, a generic **`Exception`** handler is used to catch and display any other unexpected errors that might occur during execution.

### Password Encryption:

- The **`encrypt_password(password)`** function not only encrypts the user's password but also associates it with a randomly selected superhero name (**`hero`**) and a random number (**`number`**). This adds an extra layer of security by using unique identifiers for each encryption instance.

### File Handling:

- The script utilizes file handling to store and retrieve encrypted password data. It checks if the file named 'Encrypt.pkl' exists before attempting to load data from it. If the file does not exist, it initializes an empty list to store password data.
- When encrypting a password, it first checks if the file exists and loads existing password data from it. After encrypting a new password, it appends the encrypted data to the existing list and saves it back to the file.
- This approach ensures that previously encrypted passwords are not overwritten, and new passwords are added to the existing database of encrypted passwords.

### User Input Validation:

- The script validates user input to ensure that it meets certain criteria before proceeding with encryption, decryption, or other operations. For example, in the **`encrypt_user_password()`** function, it checks if the password provided by the user is at least 12 characters long before proceeding with encryption.
- Similarly, in the **`decrypt_password()`** function, it prompts the user to enter a hero and a number and validates the input to ensure that it matches the format expected for hero names and numbers.

### Randomness and Security:

- Randomness is introduced at various points in the code to enhance security. For example, when generating passwords, selecting superheroes, and generating RSA key pairs, randomization ensures that the encryption process is not predictable, making it more resistant to attacks.

### Modular Design:

- The code follows a modular design approach, with each function responsible for a specific task. This makes the code easier to understand, maintain, and debug.
- By breaking down the functionality into smaller, reusable components, the code promotes code reusability and readability, adhering to best practices in software engineering.
