#secret message:
secret_message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
new_message = "hey there! this is an example of a caesar cipher. were you able to decode it? i hope so! send me a message back with the same offset!"
offset = 10
cipher = {}
alpha = "abcdefghijklmnopqrstuvwxyz"

def createCipher(string):
    for letter in string:
        i = string.index(letter)
        cipher[i] = letter
    return cipher

createCipher(alpha)
print(cipher)

def DecodeCipher(message, offset):
    createCipher(alpha)
    decodedMessage = ""
    letter_list = list(cipher.values())

    for char in message:
        if char not in letter_list:
            decodedMessage = decodedMessage + char
        
        else: 
            value = letter_list.index(char)
            newValue = value + offset

            if newValue > 25:
                newValue = (newValue - 26)
                # print(newValue)
                # print(newValue)
            decodedChar = cipher[newValue]
            # print(decodedChar)
            decodedMessage = decodedMessage + decodedChar
            # print(decodedMessage)
    print(decodedMessage)
    return decodedMessage

def codeMessage(message, offset):
    createCipher(alpha)
    codedMessage = ""
    letter_list = list(cipher.values())

    for char in message:
        if char not in letter_list:
            codedMessage = codedMessage + char
        
        else: 
            value = letter_list.index(char)
            newValue = value - offset

            if newValue < 0:
                newValue = 26 - (offset - value)
                # print(newValue)
                # print(newValue)
            codedChar = cipher[newValue]
            # print(decodedChar)
            codedMessage = codedMessage + codedChar
            # print(decodedMessage)
    print(codedMessage)
    return codedMessage

print(DecodeCipher(secret_message, 10))
print(codeMessage(new_message, 10))