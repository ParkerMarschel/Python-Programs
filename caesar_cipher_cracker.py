import optparse

"""
Function: hack()
Algorithm: Takes in a string message to attempt to crack by
           brute forcing to test every possible key. Uses ASCII
           characters for upper and lower case. Space characters
           remain the same.
"""
def hack(msg):
   # Loops through every key
   for k in range(26):
      strOut = ""
      #Loops through the message
      for symbol in msg:
         # Checks for upper-case
         if symbol.isupper():
            value = ord(symbol) - 65
            value = value - k
            if value < 0:
               value = value + 26
            strOut = strOut + chr(value + 65)
         # Checks for upper-case
         elif symbol.islower():
            value = ord(symbol) - 97
            value = value - k
            if value < 0:
               value = value + 26
            strOut = strOut + chr(value + 97)
         # For spaces
         else:
           strOut = strOut + symbol
      # Outputs the message corresponding to the key that was used
      print("Key: " + str(k) + " ---- Decryption: " + strOut + "\n")



def main():
    parser = optparse.OptionParser("usage%prog "+ "-m <message>")
    parser.add_option('-m', dest='msg', type='string',  help='message to hack')
    (options, args) = parser.parse_args()
    msg = str(options.msg)
    if msg == None:
        print('[-] You must specify a message and k.')
        exit(0)
    else:
        hack(msg)

if __name__ == '__main__':
    main()
