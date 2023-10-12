#secret message:
secret_message = "xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!"
new_message = "hey there! this is an example of a caesar cipher. were you able to decode it? i hope so! send me a message back with the same offset!"
offset = 10
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
    createCipher(alpha)
    decodedMessage = ""

    #create keyword phrase
def create_keyword_phrase(keyword, secret_message):
    keyword_phrase = ""
    k = 0
    
    for i in secret_message:
        if k > len(keyword):
            k = 0
        else:
            if secret_message[i] not in letter_list:
                keyword_phrase[i] = secret_message[i]
            keyword_phrase = keyword_phrase + keyword[i]
            i += 1
        
    print(keyword_phrase)
    return keyword_phrase
            
create_keyword_phrase("cat", "ciphers are awesome!")

 



