from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import os
import base64

def encrypt_string(password, plaintext):
    # Generate a random salt for the key derivation
    salt = os.urandom(16)

    # Derive the encryption key from the password using PBKDF2
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # 32 bytes for a 256-bit key
        salt=salt,
        iterations=100_000,  # Adjust the number of iterations as per your requirements
    )
    encryption_key = kdf.derive(password.encode())

    # Encode the encryption key as URL-safe base64
    encoded_key = base64.urlsafe_b64encode(encryption_key)

    # Create the cipher suite using the derived encryption key
    cipher_suite = Fernet(encoded_key)

    # Encrypt the plaintext
    ciphertext = cipher_suite.encrypt(plaintext.encode())

    # Return the encrypted ciphertext and the salt used for key derivation
    return ciphertext, salt

def decrypt_string(password, ciphertext, salt):
    # Derive the encryption key from the password and salt using PBKDF2
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # 32 bytes for a 256-bit key
        salt=salt,
        iterations=100_000,  # Same number of iterations used during encryption
    )
    encryption_key = kdf.derive(password.encode())

    # Encode the encryption key as URL-safe base64
    encoded_key = base64.urlsafe_b64encode(encryption_key)

    # Create the cipher suite using the derived encryption key
    cipher_suite = Fernet(encoded_key)

    # Decrypt the ciphertext
    decrypted_text = cipher_suite.decrypt(ciphertext)

    # Return the decrypted plaintext
    return decrypted_text.decode()


