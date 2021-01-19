import optparse

"""
Function: encrypt()
Algorithm: Takes in a message and a key and encypts using
           the caesar cipher algorithm. Returns the encrypted
           text.
"""
def encrypt(msg, key):
    # finds the length of the message to taverse
    # output message after encyrtion
    strOut = ""
    msgLen = len(msg)
    for index in range(msgLen):
        # current character in the messahe
        ltr = msg[index]
        # Checks if the character is upper case
        if(ltr.isupper()):
            # Gets the ASCII character value to use for modulus division
            # switches plaintext to encypted character
            newLtr = chr((ord(ltr) + key - 65) % 26 + 65)
            # Places the encoded character into return string
            strOut += newLtr
        # For lower-case letters
        elif(ltr.islower()):
            # <Line 13>
            newLtr = chr((ord(ltr) + key - 97) % 26 + 97)
            strOut += newLtr
        # Accounts for spaces
        else:
            strOut += ltr
    # Returns encrypted message
    return strOut


"""
Function: decrypt()
Algorithm: The same as the encyption function except
           it decrypts the message with a key.
"""
def decrypt(msg, key):
    strOut = ""
    msgLen = len(msg)
    for index in range(msgLen):
        # current character in the message
        ltr = msg[index]
        # Checks if the character is upper case
        if(ltr.isupper()):
            # switches the encypted character back to plaintext
            newLtr = chr((ord(ltr) - key - 65) % 26 + 65)
            strOut += newLtr
        # For lower-case letters
        elif(ltr.islower()):
            newLtr = chr((ord(ltr) - key - 97) % 26 + 97)
            strOut += newLtr
        else:
            strOut += ltr
    # Returns decrypted message
    return strOut


def main():
    parser = optparse.OptionParser("usage%prog "+ "-f <decrypt | encrypt> -m <message> -k <key>")
    parser.add_option('-f', dest='function', type='string', help='[ decrypt | encrypt ]')
    parser.add_option('-m', dest='msg', type='string',  help='message to encrypt (plaintext) or decrypt (encrypted)')
    parser.add_option('-k', dest='key', type='string', help='cipher key as an integer')
    (options, args) = parser.parse_args()
    function = options.function
    if ((function != "encrypt" and function != "decrypt") or function == None):
        print('[-] You must specify a valid function: "encrypt" or "decrypt"')
        exit(0)
    msg = str(options.msg)
    key = int(options.key)
    if (msg == None) | (key == None):
        print('[-] You must specify a message and key.')
        exit(0)
    if function == "encrypt":
        print(encrypt(msg, key))
    elif function == "decrypt":
        print(decrypt(msg, key))

if __name__ == '__main__':
    main()
