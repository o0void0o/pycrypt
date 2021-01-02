from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES

key = get_random_bytes(32) # 32 bytes * 8 = 256 bits (1 byte = 8 bits)
print(key)



output_file = 'enc/encrypted.bin'
file = open("supernoooichFile.adoc", "rb")
data = file.read(-1)


cipher = AES.new(key, AES.MODE_CFB) # CFB mode
ciphered_data = cipher.encrypt(data) # Only need to encrypt the data, no padding required for this mode

file_out = open(output_file, "wb")
file_out.write(cipher.iv)
file_out.write(ciphered_data)
file_out.close()


input_file= 'enc/encrypted.bin'

file_in = open(input_file, 'rb')
iv = file_in.read(16)
ciphered_data = file_in.read()
file_in.close()

cipher = AES.new(key, AES.MODE_CFB, iv=iv)
original_data = cipher.decrypt(ciphered_data) # No need to un-pad
print(original_data)
f = open('dec/lkjl.adoc', 'wb')
f.write(original_data)
f.close()

#https://nitratine.net/blog/post/python-encryption-and-decryption-with-pycryptodome/
