from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import sys

def keygen(size):
    valid_sizes = [1024, 2048, 3072 ,4096]
    
    if size not in valid_sizes:
        return -1

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=size,
    )
    return private_key

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print("Usage: python3 keygen.py <pubkeyfile> <privkeyfile> <size>")
        sys.exit(1)

    key = keygen(int(sys.argv[3]))

    if key == -1:
        print("Invalid key size")
        sys.exit(1)
    
    with open(sys.argv[1], "wb") as f:
        f.write(key.public_key().public_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PublicFormat.SubjectPublicKeyInfo
        ))
    with open(sys.argv[2], "wb") as f:
        f.write(key.private_bytes(
            encoding=serialization.Encoding.PEM,
            format=serialization.PrivateFormat.PKCS8,
            encryption_algorithm=serialization.NoEncryption()
        ))