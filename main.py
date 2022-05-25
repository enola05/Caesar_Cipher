alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def encrypt(text,shift):
  c=""
  for i in range(0,len(text)):
    k=alphabet.index(text[i])
    c+=alphabet[k+shift]
  print(f'The encoded text is {c}')

def decrypt(text,shift):
  c=""
  for i in range(0,len(text)):
    k=alphabet.index(text[i])
    c+=alphabet[k-shift]
  print(f'The decoded text is {c}')

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
if direction=="encode":
  encrypt(text,shift)
else:
  decrypt(text,shift)


