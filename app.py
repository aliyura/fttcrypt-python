from fttcrypt import FTTCryptor

key = "SecretKeyGoesHere"
text="Secured to to be encrypted"

# Encrypt a plain Text to Cipher
cipherText = FTTCryptor.encryptText(text, key)
print(cipherText)


# Decrypt Cipher to Plain Text
decryptedText = FTTCryptor.decryptText(cipherText, key)
print(decryptedText)


# Encrypt a file to Cipher
cipherText = FTTCryptor.encryptFile("file.jpg", key)
print(cipherText)

# Decrypt Cipher to File
file = FTTCryptor.decryptFile(cipherText, key)
print(file)
