from cryptography.hazmat.primitives import padding


def addpadding(plaintext):
	padder = padding.PKCS7(128).padder()

	padded_data = padder.update(bytes.fromhex(plaintext))

	padded_data += padder.finalize()

	print(padded_data)
	return padded_data.hex()

def removepadding(padded_data):
	unpadder = padding.PKCS7(128).unpadder()

	data = unpadder.update(padded_data)

	data + unpadder.finalize()

	print(data.hex())
