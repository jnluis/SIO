from cryptography.hazmat.primitives import hashes

digest = hashes.Hash(hashes.SHA256())

digest.update(b"1024")

digest.finalize()
