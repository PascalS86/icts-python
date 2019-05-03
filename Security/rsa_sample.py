def encrypt(n_pk, n_plaintext):
    #Unpack the key into it's components
    key, n = n_pk
    #Convert each letter in the n_plaintext to numbers based on the character using a^b mod m
    cipher = [(ord(char) ** key) % n for char in n_plaintext]
    #Return the array of bytes
    return cipher


def decrypt(n_pk, ciphertext):
    #Unpack the key into its components
    key, n = n_pk
    #Generate the n_plaintext based on the ciphertext and key using a^b mod m
    plain = [chr((char ** key) % n) for char in ciphertext]
    #Return the array of bytes as a string
    return ''.join(plain)

print("RSA Encrypter/ Decrypter")

public, private = ((29,35), (5,35))

message = chr(12)

encrypted_msg = encrypt(private, message)

print("Your encrypted message is: ")
print(encrypted_msg)
print("Decrypting message with public key ", public ,"...")
print("Your message is:")
print(ord(decrypt(public, encrypted_msg)))

#https://github.com/dlitz/pycrypto