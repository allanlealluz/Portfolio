def rot13(message):
    result = list()
    encript_message = []
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabet2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    for word in message:
        if not word.isalpha():
            result.append(word)
        else:
            if word.isupper() and word.isalpha():
                position = alphabet2.find(word)+1
                encode = position + 13
            elif word.isalpha():
                position = alphabet.find(word.lower())+1
                encode = position + 13
            if encode > 26:
                result.append(encode - 26)
            else:
                result.append(encode)
            print(result)
    for c,i in enumerate(result):
        if message[c].isupper() and int(i) <= 26:
            encript_message.append(alphabet2[int(i-1)])
        elif message[c].islower() and int(i) <= 26 :
            encript_message.append(alphabet[int(i-1)])
        else:
            encript_message.append(str(i))
    encript_message = ''.join(encript_message)
    print(encript_message)
rot13("test")
rot13("Test")
rot13("12Test")
rot13('T5yFnHv2kcgRvgMT')
