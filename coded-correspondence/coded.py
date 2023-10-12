#secret message:
secret_message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
new_message = "hey there! this is an example of a caesar cipher. were you able to decode it? i hope so! send me a message back with the same offset!"
offset = 10
#value:letter
cipher = {}
alpha = "abcdefghijklmnopqrstuvwxyz"
letter_list = list(cipher.values())

def createCipher(string):
    for letter in string:
        i = string.index(letter)
        cipher[i] = letter
    return cipher

createCipher(alpha)
# print(cipher)

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

# print(DecodeCipher(secret_message, 10))
# print(codeMessage(new_message, 10))

#Decoding message when you don't know the offset:
# encoded_message = "vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx."
# for i in range(0, 26):
#     DecodeCipher(encoded_message, i)


#Vigenere Cipher
m = "txm srom vkda gl lzlgzr qpdb? fepb ejac! ubr imn tapludwy mhfbz cza ruxzal wg zztcgcexxch!"
key = "friends"

def decode_vigenere(secret_message, keyword):
    decodedMessage = ""

    #create keyword phrase
    keyword_phrase = ""
    k_index = 0
    
    for char in secret_message:
        if k_index >= len(keyword):
            k_index = 0
        if char in alpha:
            keyword_phrase += keyword[k_index]
            k_index += 1
        else:
            keyword_phrase += char
        
    for i in range(len(secret_message)):
        if secret_message[i] not in alpha:
            decodedMessage += secret_message[i]
        else:
            value_index = alpha.find(secret_message[i])
            offset_index = alpha.find(keyword_phrase[i])
            new_char = alpha[(value_index + offset_index) % 26]
            decodedMessage += new_char

    print(decodedMessage)
    return decodedMessage

decode_vigenere("aiwfeyq ayc adcsvke!", "cat")

 
def encode_vigenere(secret_message, keyword):
    encodedMessage = ""

    #create keyword phrase
    keyword_phrase = ""
    k_index = 0
    
    for char in secret_message:
        if k_index >= len(keyword):
            k_index = 0
        if char in alpha:
            keyword_phrase += keyword[k_index]
            k_index += 1
        else:
            keyword_phrase += char
        
    for i in range(len(secret_message)):
        if secret_message[i] not in alpha:
            encodedMessage += secret_message[i]
        else:
            value_index = alpha.find(secret_message[i])
            offset_index = alpha.find(keyword_phrase[i])
            new_char = alpha[(value_index - offset_index) % 26]
            encodedMessage += new_char

    print(encodedMessage)
    return encodedMessage

encode_vigenere("ciphers are awesome!", "cat")


