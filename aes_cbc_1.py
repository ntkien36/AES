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
   data_bytes= bytes (plaintext,'utf-8')
   padded_bytes=pad (data_bytes, AES.block_size)
   AES_obj=AES.new (key, AES.MODE_CBC, iv)
   ciphertext=AES_obj.encrypt (padded_bytes)
   return ciphertext
ciphertext= encrypt (plaintext)
print ('Ciphertext:',binascii.hexlify (ciphertext))

#Decryption
def decrypt (ciphertext):
   AES_obj=AES.new (key, AES.MODE_CBC, iv)
   raw_bytes=AES_obj.decrypt (ciphertext)
   extracted_bytes = unpad (raw_bytes, AES.block_size)
   return extracted_bytes
plaintext = decrypt (ciphertext)
print ('Plaintext:',plaintext.decode ('ascii'))