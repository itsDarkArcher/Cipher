from flask import Flask, request, jsonify
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import random 
import string
import sqlite3

app = Flask(__name__)

heroes = ['Superman', 'Batman', 'Spider Man', 'Flash', 'Green Arrow', 'Hulk', 'Hawkeye', 'Black Panther', 'Iron Man', 'Thor']

@app.route('/generate_password', methods=['GET'])
def generate_password():
    """
    Endpoint to generate a random password with hyphens and periods randomly placed
    """
    try:
        # Generate a random password
        characters = string.ascii_letters + string.digits
        password = ''.join(random.choice(characters) for _ in range(18))
        
        # Insert hyphens and periods randomly
        special_chars ='-.'
        num_special_chars = random.randint(1,4) # Choose the number of special characters to put randomly
        for _ in range(num_special_chars):
            position = random.randint(0, len(password)) # Choose the random position for the char
            special_char = random.choice(special_chars)
            password = password[:position] + special_char + password[position:]
            
        return jsonify({"password": password}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route("/encrypt_password", methods=['POST'])
def encrypt_password():
    """
    Endpoint to encrypt given password
    """
    try:
        data = request.get_json()
        password = data['password']
        
        # Select random hero and number
        hero = random.choice(heroes).replace(" ","")
        number = random.randint(0, 99)
        
        # Generate RSA pair
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
        
        return jsonify({
            "hero": hero,
            "number":number
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route('/decrypt_password', methods=['POST'])
def decrypt_password():
    """
    Endpoint to decrypt a password.
    """
    try:
        data = request.get_json()
        hero = data["hero"]
        number = data["number"]
        cipher_data = load_data(hero, number)
        if cipher_data is not None:
            password = decrypt(cipher_data)
            if password is not None:
                return jsonify({'password': password}), 200
            else:
                return jsonify({"message": "Password could not be decrypted."}), 400
        else:
            return jsonify({"message": "Hero and number not found."}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def decrypt(cipher_data):
    """
    Decrypts the password using the private key.
    """
    try:
        # Decrypt the password using the private key
        private_key = RSA.import_key(cipher_data['private_key'])
        cipher = PKCS1_OAEP.new(private_key)
        password = cipher.decrypt(cipher_data['password'])
        return password.decode()
    except Exception as e:
        print(f"Error decrypting password: {e}. Please try again.")
        return None
    
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
    """
    Sets up the database if it doesn't exist
    """
    try:
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
    except sqlite3.Error as e:
        print(f"Error setting up database: {e}")
        
if __name__ == "__main__":
    setup_database()
    app.run(debug=True)

