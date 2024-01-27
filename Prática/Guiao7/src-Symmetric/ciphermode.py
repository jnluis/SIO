import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from padding import addpadding, removepadding

#AES-128 TEST
KEY         = "edfdb257cb37cdf182c5455b0c0efebb"
PLAINTEXT   = "1695fe475421cace3557daca01f445ff"
#CIPHERTEXT  = 7888beae6e7a426332a7eaa2f808e637

def ecb(key, plaintext):
	key= bytes.fromhex(key)
	plaintext= bytes.fromhex(plaintext)
	cipher = Cipher(algorithms.AES(key), modes.ECB())

	encryptor = cipher.encryptor()

	ct = encryptor.update(plaintext) + encryptor.finalize()

	print(ct.hex())

	decryptor = cipher.decryptor()

	dct = decryptor.update(ct) + decryptor.finalize()

	print(dct.hex())
	return dct

ecb(KEY, PLAINTEXT)

#AES-128-ECB TEST
KEY2         = "7723d87d773a8bbfe1ae5b081235b566"
PLAINTEXT2   = "1b0a69b7bc534c16cecffae02cc5323190ceb413f1db3e9f0f79ba654c54b60e"
#CIPHERTEXT  = ad5b089515e7821087c61652dc477ab1f2cc6331a70dfc59c9ffb0c723c682f6
print("AES-128-ECB TEST")
ecb(KEY2, PLAINTEXT2)

#AES-128-CBC TEST
KEY3         = "0700d603a1c514e46b6191ba430a3a0c"
IV          = "aad1583cd91365e3bb2f0c3430d065bb"
PLAINTEXT3   ="068b25c7bfb1f8bdd4cfc908f69dffc5ddc726a197f0e5f720f730393279be91"
#CIPHERTEXT  = c4dc61d9725967a3020104a9738f23868527ce839aab1752fd8bdb95a82c4d00

print("AES-128-CBC-TEST")


def cbc(key, plaintext, iv):
	key = bytes.fromhex(key)
	plaintext = bytes.fromhex(plaintext)
	iv = bytes.fromhex(iv)
	cipher = Cipher(algorithms.AES(key), modes.CBC(iv))

	encryptor = cipher.encryptor()

	ct = encryptor.update(plaintext) + encryptor.finalize()

	print(ct.hex())

	decryptor = cipher.decryptor()

	dct = decryptor.update(ct) + decryptor.finalize()

	print(dct.hex())


cbc(KEY3, PLAINTEXT3, IV)

#AES-128 TEST PADDING
KEY         = "edfdb257cb37cdf182c5455b0c0efebb"
PLAINTEXT   = "00"
#CIPHERTEXT  = 1c8cf23a5999dc4b8ae7b52f8c471225
print("TEST PADDING" )

padded = addpadding(PLAINTEXT)
ecb_result = ecb(KEY, padded)

removepadding(ecb_result)
#removepadding(padded)
#AES-128-ECB TEST PADDING
KEY2         = bytes.fromhex("7723d87d773a8bbfe1ae5b081235b566")
PLAINTEXT2   = bytes.fromhex("1b0a69b7bc534c16cecffae02cc5323190ceb413f1db3e9f0f79ba654c54b601")
#CIPHERTEXT  = ad5b089515e7821087c61652dc477ab13ee2e6dcbc921409cd7060ea9d2945792cb90e7912c7c42662a651db32a313a5
print("TEST ECB PADDING")
padded2 = addpadding(PLAINTEXT2)
ecb_result2 = ecb =(KEY2, padded2)
removepadding(ecb_result2)

#AES-128-CBC TEST PADDING
KEY         = bytes.fromhex("0700d603a1c514e46b6191ba430a3a0c")
IV          = bytes.fromhex("aad1583cd91365e3bb2f0c3430d065bb")
PLAINTEXT   = bytes.fromhex("068b25c7bfb1f8bdd4cfc908f69dffc5ddc726a197f0e5f7")
#CIPHERTEXT  = c4dc61d9725967a3020104a9738f2386b2a3deac1540e33e42c5a19e60152ce4
