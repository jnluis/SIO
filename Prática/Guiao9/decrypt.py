from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization
import sys

def decrypt(original_file, priv_key_file):
    privkey = None

    with open(priv_key_file, "rb") as f:
        privkey = serialization.load_pem_private_key(
            f.read(),
            password=None,
        )

    decrypted_message = []
    with open(original_file, "rb") as f:
        while True:
            ciphertext = f.read(privkey.key_size // 8)
            if not ciphertext:
                break 
            decrypted_message.append(privkey.decrypt(
                ciphertext,
                padding.PKCS1v15(),
            )
            )  
    return decrypted_message

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python3 decrypt.py <file_to_decrypt> <privkeyfile> <decrypted_file>")
        sys.exit(1)

    decrypted_data = decrypt(sys.argv[1], sys.argv[2])
    
    with open(sys.argv[3], "wb") as f:
        for decrypted_message in decrypted_data:
            f.write(decrypted_message)