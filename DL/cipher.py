import argparse
import Crypto.Cipher.AES as aes  #pip install pycryptodome
parser = argparse.ArgumentParser()
parser.add_argument("src", help="File to encrypt")
parser.add_argument("dest", help="Name of the cipher file")
args = parser.parse_args()
print(f"Load {args.src}")
with open(args.src,"rb") as f:
    data = f.read()
key = b'Mesulog & Cyril!'
nonce=b'\xa1TD\xdc\xde\x0b\xfc\xc8\xa1\xdc()DuZb'
cipher = aes.new(key, aes.MODE_EAX,nonce=nonce)
print(f"Cipher {args.src}")
ciphertext, tag = cipher.encrypt_and_digest(data)
print(f"Generate {args.dest}")
with open(args.dest,"wb") as f:
    f.write(ciphertext)
print("Verify")
with open(args.dest,"rb") as f:
    data = f.read()
cipher = aes.new(key, aes.MODE_EAX,nonce=nonce)
data = cipher.decrypt(data)
cipher.verify(tag)




