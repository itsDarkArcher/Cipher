from project import *

# Test the generate_password function
def test_generate_password():
    password = generate_password()
    assert len(password) == 18

# Test the encrypt_password function
def test_encrypt_password():
    password = "testpassword"
    hero, number, _, _ = encrypt_password(password)
    assert isinstance(hero, str)
    assert isinstance(number, int)

# Test the decrypt function
def test_decrypt():
    password = "testpassword"
    _, _, _, cipher_data = encrypt_password(password)
    decrypted_password = decrypt(cipher_data)
    assert decrypted_password == password

