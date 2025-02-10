#todo encrytion code

import random
import string

chars = " " + string.punctuation + string.ascii_letters + string.digits
chars = list(chars)
key = chars.copy()

random.shuffle(key)

print(f"chars: {chars}")
print(f"key: {key}")
#todo encrypte

plain_text = input("Enter your message: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"Cipher text: {cipher_text}")
print(f"Plain text: {plain_text}")

cipher_text = input("Enter your message: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"Cipher text: {cipher_text}")
print(f"Plain text: {plain_text}")