#Authors: Ricardus Hasbani, Hamza Khawaja

from PIL import Image
import random
import hashlib

def vigenere(val): # Original Vigenere Encryption/Decryption: C = (P + K) % 26 & P = (C - K) % 26
    pe = key[k] + val
    if pe >= 256:
        pe = pe % 256 #In our scenario, Z26 is equivalent to Z256
    if pe < 0:
        pe = pe + 256
    return pe

def decrypt(val):
    pd = val - key[k]
    if pd < 0:
        pd = pd + 256
    if pd >= 256:
        pd = pd % 256
    return pd

def keygen(width):
    key = [random.randint(1,255) for _ in range(width)] #generates a random key based on the width of an image
    return key

random.seed = input("input seed: ") #allows for users to share seeds

im = Image.open(r"C:\Users\ricar\Desktop\___\chipsa_clear.png")
im = im.convert("RGB")
px = im.load()
md5hash_original = hashlib.md5(im.tobytes()) #Used for confirmation of no pixel loss

width, height = im.size
key = keygen(width)

pv = list(im.getdata()) #grabs all tuples from the image and stores them into list
print("Encrypting...")
k = 0
for i in range(width):
    for j in range(height):
        key[k]
        px[i,j] = (vigenere(px[i,j][0]), vigenere(px[i,j][1]), vigenere(px[i,j][2])) #px[i,j] is a variable for the tuple,
        k = (k + 1) % len(key) # cycles through key for each tuple
im = im.save("NewImage.png")

im2 = Image.open(r"C:\Users\ricar\PycharmProjects\Crypto_FinalProject\NewImage.png")
px2 = im2.load()

width, height = im2.size

pv2 = list(im2.getdata())
print("Decrypting...")
for i in range(width):
    for j in range(height):
        key[k]
        px2[i,j] = (decrypt(px2[i,j][0]), decrypt(px2[i,j][1]), decrypt(px2[i,j][2])) #px2[i,j] is a variable for the encrypted images tuple
        k = (k + 1) % len(key) #cycles through key for each tuple

im2 = im2.save("BacktoNormal.png")

md5hash_new = hashlib.md5(Image.open('BacktoNormal.png').tobytes()) #Used for confirmation of no pixel loss
print("Key length: " + str(len(key)) + " " + "\nkey: " + str(key))
print(f"md5 hash of input image (before encryption): {md5hash_new.hexdigest()} md5 hash of decrypted image: {md5hash_original.hexdigest()}")

