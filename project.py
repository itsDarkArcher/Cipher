import random
import pickle
import string
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import os
import sys

# List of heroes for the password encryption
heroes = ['Superman', 'Batman', 'Spider Man', 'Flash', 'Green Arrow', 'Hulk', 'Hawkeye', 'Black Panther', 'Iron Man', 'Thor']

def main():
    """
    main function to execute the program
    """
    while True:
        print("Choose from the following options (1, 2, 3, 4):\n1 - Encrypt User Password\n2 - Generate Encrypted Password\n3 - Decrypt Password\n4 - Exit ")

        try:
            option = input("Selected Option: ").strip().lower()

            if option == "1":
                encrypt_user_password()

            elif option == "2":
                generate_encrypted_password()

            elif option == "3":
                decrypt_password()

            elif option == "4":
                print("\nThis was CS50.")
                sys.exit()

            else:
                print("\nInvalid option. Please select a valid option (1, 2, 3, 4).")

        except KeyboardInterrupt:
            print("\nThis was CS50.")
            sys.exit()
        except Exception as e:
            print(f"\nError: {e}")

def generate_password():
    """
    Generates a random password with hyphens and periods randomly placed
    """
    try:
        # Generate a random password
        characters = string.ascii_letters + string.digits
        password_length = 18
        password = ''.join(random.choice(characters) for _ in range(password_length))

        # Insert hyphens and periods randomly
        special_chars = '-.'
        num_special_chars = random.randint(1, 4)  # Randomly choose the number of special characters
        for _ in range(num_special_chars):
            position = random.randint(0, len(password))  # Random position to insert special character
            special_char = random.choice(special_chars)
            password = password[:position] + special_char + password[position:]

        return password
    except Exception as e:
        print(f"Error generating password: {e}. Please try again.")

def encrypt_password(password):
    """
    Encrypts given password
    """
    try:
        # Select a random hero and number
        hero = random.choice(heroes).replace(" ", "")
        number = random.randint(0, 99)

        # Generate RSA key pair
        key = RSA.generate(2048)
        cipher = PKCS1_OAEP.new(key)
        # Encrypt the password
        encrypted_password = cipher.encrypt(password.encode())

        # Store encrypted password and associated data
        cipher_data = {
            "hero": hero,
            "number": number,
            "password": encrypted_password,
            "private_key": key.export_key()
        }

        # Check if the pickle file exists
        if os.path.exists('Encrypt.pkl'):
            # If the file exists, load the existing passwords
            with open('Encrypt.pkl','rb') as f:
                existing_passwords = pickle.load(f)
        else:
            # If the file doesn't exist, initialize an empty list
            existing_passwords = []

        # Append the new encrypted password to the list
        existing_passwords.append(cipher_data)

        # Save the updated list of encrypted passwords to the pickle file
        with open('Encrypt.pkl', 'wb') as f:
            pickle.dump(existing_passwords, f)

        return hero, number, password, cipher_data
    except Exception as e:
        print(f"Error encrypting password: {e}. Please try again.")

def decrypt_password():
    """
    Decrypts a password.
    """
    while True:
        try:
            hero = input("Enter the hero: ").replace(" ", "")
            number = int(input("Enter the number: "))
            cipher = load_data(hero, number)
            if cipher is not None:
                password = decrypt(cipher)
                if password is not None:
                    print(f"The generated password is: {password}")
                    break
                else:
                    print("The password could not be decrypted.")
            else:
                print("The specified hero and number were not found.")
        except Exception as e:
            print(f"\nError: {e}")

def load_data(hero, number):
    """
    Loads data from the file and searches for matching hero and number.
    """
    try:
        # Load data from file and search for matching hero and number
        with open('Encrypt.pkl', 'rb') as file:
            password = pickle.load(file)
            for cipher_data in password:
                if cipher_data['hero'] == hero and cipher_data['number'] == number:
                    return cipher_data
            return None
    except FileNotFoundError:
        print("The file 'Encrypt.pkl' is not found. Please make sure you have generated a password first.")
        return None
    except (KeyError):
        print("No valid data found in the 'Encrypt.pkl' file.")
        print("Generate a password first.")
        return None

def decrypt(cipher_data):
    """
    Decrypts the password using the private key.
    """
    try:
        # Decrypt the password using the private key
        if cipher_data is not None:
            private_key = RSA.import_key(cipher_data['private_key'])
            cipher = PKCS1_OAEP.new(private_key)
            password = cipher.decrypt(cipher_data['password'])
            return password.decode()
    except Exception as e:
        print(f"Error decrypting password: {e}. Please try again.")

def encrypt_user_password():
    while True:
        try:
            password = input("Enter the password to encrypt: ")
            if len(password) >= 12:
                hero, number, _, cipher = encrypt_password(password)
                hero = ''.join(' ' + i if i.isupper() else i for i in hero).lstrip(' ')
                print(f"A password was encrypted with the hero {hero} and the number {number}.")
                break
            else:
                print("The password must contain at least 12 characters")
        except Exception as e:
            print(f"\nError: {e}")

def generate_encrypted_password():
    """
    Generates and encrypts a random password.
    """
    while True:
        try:
            password = generate_password()
            hero, number, _, cipher = encrypt_password(password)
            hero = ''.join(' ' + i if i.isupper() else i for i in hero).lstrip(' ')
            print(f"The password {password} was generated and encrypted with the hero {hero} and number {number}.")
            break
        except Exception as e:
            print(f"\nError: {e}")

if __name__ == "__main__":
    main()
