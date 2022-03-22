alphabet  = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key       = "UHQKRNWLFIYJBTODCZVAXEGSMP"

cipher_text = ""

with open("message.txt", "r") as f:
    # it is important to use .read() here as it exports the file as 
    # a string rather than a list of lines (a la .readlines())
    cipher_text = f.read()

# zip creates a tuple of tuples, dict creates key-value mappings from it
keyMap = dict(zip(key, alphabet))
# .get(keyname, value) where value is the value to return if the keyname does not exist
unscrambled = ''.join(keyMap.get(c.upper(), c) for c in cipher_text)

print('Unscrambled text:\n--')
print(unscrambled)
print("\n--\n")
# unnecessary, but fun
print(f"picoCTF{unscrambled[unscrambled.index('PICOCTF') + 7:]}")

a_day = ["Steven", "Alexander", "Joseph", "Miranda", "Marabel"]
b_day = ["Alexa", "Sasha", "Weierstrauss", "John"]

print(list(zip(a_day, b_day)))