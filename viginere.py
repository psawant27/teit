text = input("Enter text you would like to encrypt: ")
key = input("Enter string key: ")

def vigenere_encrypt(text, key):
    print('_Encryption__')
    text = text.replace(' ', '')
    print('Input string:', text)

    key = list(key)
    for i in range(len(text) - len(key)):
        key.append(key[i % len(key)])
    key = "".join(key)

    result = ""
    for i in range(len(text)):
        if text[i].isupper():
            res = chr(((ord(text[i]) - 65) + (ord(key[i]) - 65)) % 26 + 65)
        else:
            res = chr(((ord(text[i]) - 97) + (ord(key[i]) - 97)) % 26 + 97)
        result += res
    print('Encrypted output: ', result)
    return result

def vigenere_decrypt(text, key):
    print('__Decryption__')
    print('Input string: ', text)

    key = list(key)
    for i in range(len(text) - len(key)):
        key.append(key[i % len(key)])
    key = "".join(key)

    result = ""
    for i in range(len(text)):
        if text[i].isupper():
            res = chr(((ord(text[i]) - 65) - (ord(key[i]) - 65) + 26) % 26 + 65)
        else:
            res = chr(((ord(text[i]) - 97) - (ord(key[i]) - 97) + 26) % 26 + 97)
        result += res
    print('Decrypted output: ', result)
    return result

encrypted = vigenere_encrypt(text, key)
decrypted = vigenere_decrypt(encrypted, key)