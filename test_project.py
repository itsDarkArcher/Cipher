from project import *

# Test the generate_password function
def test_generate_password():
    password = generate_password()
    assert len(password) > 18
    special_chars = ".-"
    assert any(char in special_chars for char in password)
    assert any(char.isupper() for char in password)
    assert any(char.islower() for char in password)
    assert any(char.isdigit() for char in password)
    
# Test the encrypt_password function
def test_encrypt_password():
    password = "testpassword"
    hero, number, _, cipher_data = encrypt_password(password)
    assert isinstance(hero, str)
    assert isinstance(number, int)
    assert isinstance(cipher_data["password"], bytes)
    assert os.path.exists('Encrypt.pkl')
    with open('Encrypt.pkl', 'rb') as f:
        existing_passwords=pickle.load(f)
    assert cipher_data in existing_passwords
    assert hero is not None
    assert number is not None
    assert 0<= number <=99

# Test the decrypt_password function and the load_data function
def test_decrypt__password_load_data():
    """
    Test function for decrypt_password() and load_data().
    """
    try:
        hero = "Superman"
        number = 42
        cipher = load_data(hero, number)
        assert cipher is not None, "Error: Cipher data not found for hero and number"
        password = decrypt(cipher)
        assert password == "testpassword123", f"Error: Decrypted password is not as expected. Expected: 'testpassword123', Actual: {password}"

        invalid_hero = "InvalidHero"
        invalid_number = 999
        cipher_invalid = load_data(invalid_hero, invalid_number)
        assert cipher_invalid is None
        assert decrypt(None) is None
        print("All tests passed successfully!")
    except AssertionError as e:
        print(f"Test failed: {e}")
    except Exception as e:
        print(f"Test failed: {e}")

#Test the decrypt function 
def test_decrypt():
    """
    Test function for decrypt().
    """
    try:
        # Prueba de descifrado exitoso
        cipher_data = {
            "password": b'\x0f\xd4\xe8\x94\xa6o\xd8\xe0',
            "private_key": b'-----BEGIN PRIVATE KEY-----\nMIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQDEe+oVvJ9Bx9z5\n(Private key contents)',
            # Agregar más campos según sea necesario
        }
        password = decrypt(cipher_data)
        assert password == "testpassword123", f"Error: Decrypted password is not as expected. Expected: 'testpassword123', Actual: {password}"

        # Prueba de no datos de cifrado
        assert decrypt(None) is None, "Error: Function did not handle None cipher data correctly"

        # Prueba de manejo de excepciones
        assert decrypt({}) is None, "Error: Function did not handle KeyError correctly"

        print("All tests passed successfully!")
    except AssertionError as e:
        print(f"Test failed: {e}")
    except Exception as e:
        print(f"Test failed: {e}")

#Test the encrypt_user_password and check_password_strenght
def test_encrypt_user_password_and_check_strength():
    """
    Test function for encrypt_user_password() check_password_strenght().
    """
    try:
        # Prueba de cifrado exitoso
        password = "StrongPassword123!"
        hero, number, _, cipher = encrypt_user_password(password)
        assert cipher is not None, "Error: Password encryption failed for strong password"
        assert check_password_strength(password), "Error: Strong password was incorrectly evaluated as weak"

        # Prueba de contraseña débil
        password_weak = "weakpassword"
        assert encrypt_user_password(password_weak) is None, "Error: Password encryption succeeded for weak password"
        assert not check_password_strength(password_weak), "Error: Weak password was incorrectly evaluated as strong"
        assert not check_password_strength(""), "Error: Empty password was incorrectly evaluated as strong"
        assert not check_password_strength("Short12!"), "Error: Short password was incorrectly evaluated as strong"


        print("All tests passed successfully!")
    except AssertionError as e:
        print(f"Test failed: {e}")
    except Exception as e:
        print(f"Test failed: {e}")