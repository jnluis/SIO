from cryptography.hazmat.primitives.asymmetric import padding, rsa
from cryptography.hazmat.primitives import serialization
import sys


def encrypt( original_file, pub_key):
    pkey = None

    with open(pub_key, "rb") as key_file:
        pkey = serialization.load_pem_public_key(
            key_file.read(),
        )

    encrypted_message = []
    with open(original_file, "rb") as f:
        while True:
            cleartext = f.read(117)
            if not cleartext:
                break 
            encrypted_message.append(pkey.encrypt(
                cleartext,
                padding.PKCS1v15(),
            )
            )  
    return encrypted_message

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python3 encrypt.py <file_to_encrypt> <pubkeyfile> <file_encrypted>")
        sys.exit(1)

    encrypted_data = encrypt(sys.argv[1], sys.argv[2])
    
    with open(sys.argv[3], "wb") as f:
        for encrypted_message in encrypted_data:
            f.write(encrypted_message)