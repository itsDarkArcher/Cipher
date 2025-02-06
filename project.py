from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import random
import string
import sqlite3
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
                print("\nBye Bye.")
                sys.exit()

            else:
                print("\nInvalid option. Please select a valid option (1, 2, 3, 4).")

        except KeyboardInterrupt:
            print("\nBye Bye.")
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
        password = ''.join(random.choice(characters) for _ in range(18))

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
        hero = random.choice(heroes)
        number = random.randint(0, 99)

        # Generate RSA key pair
        key = RSA.generate(2048)
        cipher = PKCS1_OAEP.new(key)
        # Encrypt the password
        encrypted_password = cipher.encrypt(password.encode())

        # Store encrypted password and the associated data in the db
        conn = sqlite3.connect("secure_passwords.db")
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO passwords (hero, number, encrypted_password, private_key)
        VALUES (?, ?, ?, ?)
        ''', (hero, number, encrypted_password, key.export_key().decode("utf-8")))
        conn.commit()
        conn.close()
        
        return hero, number, password, {
            "hero": hero,
            "number": number,
            "password": encrypted_password,
            "private_key": key.export_key()
        }
    except Exception as e:
        print(f"Error encrypting password: {e}. Please try again.")

def decrypt_password():
    """
    Decrypts a password.
    """
    while True:
        try:
            hero = input("Enter the hero: ")
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
            setup_database()
            password = input("Enter the password to encrypt: ")
            if check_password_strength(password):
                hero, number, _, cipher = encrypt_password(password)
                print(f"A password was encrypted with the hero {hero} and the number {number}.")
                break
            else:
                print("The password must contain at least 12 characters, with at least 1 uppercase, 1 lowercase, a digit and a special character.")
        except Exception as e:
            print(f"\nError: {e}")

def generate_encrypted_password():
    
    """
    Generates and encrypts a random password.
    """
    while True:
        try:
            setup_database()
            password = generate_password()
            hero, number, _, cipher = encrypt_password(password)
            print(f"The password {password} was generated and encrypted with the hero {hero} and number {number}.")
            break
        except Exception as e:
            print(f"\nError: {e}")

def check_password_strength(password):
    """
    Checks the strength of a password.
    Returns True if the password meets the criteria, False otherwise.
    """
    
    # Check if the password meets the criteria
    if len(password) < 12:
        return False
    if not any(char.isupper() for char in password):
        return False
    if not any(char.islower() for char in password):
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char in '-.' for char in password):
        return False

    return True

def load_data(hero, number):
    """
    Loads data from the database and searches for matching hero and number.
    """
    try:
        # Load data from db and search for matching hero and number
        conn = sqlite3.connect("secure_passwords.db")
        cursor = conn.cursor()
        cursor.execute('''
        SELECT encrypted_password, private_key FROM passwords WHERE hero=? AND number=?
        ''', (hero, number))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            encrypted_password, private_key = row
            return {
                "hero": hero,
                "number": number,
                "password": encrypted_password,
                "private_key": private_key
            }
        return None
    except sqlite3.Error as e:
        print(f"Error loading data: {e}. Please try again.")
        return None
    
def setup_database():
    conn = sqlite3.connect("secure_passwords.db")
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS passwords (
        id INTEGER PRIMARY KEY,
        hero TEXT NOT NULL,
        number INTEGER NOT NULL,
        encrypted_password BLOB NOT NULL,
        private_key TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    main()
