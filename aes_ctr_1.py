from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import binascii

#inputs
plaintext = input('Plaintext..:')
pwd = input('Password..: ')
key = pad (pwd.encode(), AES.block_size)
iv = get_random_bytes(AES.block_size)


#Encryption
def encrypt (plaintext):
    data_bytes=bytes (plaintext, 'utf-8')
    #padded bytes-pad (data_bytes, AES.block_size)
    AES_obj=AES.new (key, AES.MODE_CTR)
    ciphertext=AES_obj.encrypt (data_bytes)
    return ciphertext, AES_obj.nonce
ciphertext,nonce = encrypt (plaintext)
print ('Ciphertext:',binascii.hexlify (ciphertext))

#Decryption
def decrypt (ciphertext,nonce):
    AES_obj=AES.new (key, AES.MODE_CTR, nonce = nonce)
    raw_bytes = AES_obj.decrypt(ciphertext)
    #extracted bytes-unpad (raw_bytes, AES.block_size)
    return raw_bytes
plaintext = decrypt(ciphertext,nonce)
print ('Plaintext:',plaintext.decode ('ascii'))
