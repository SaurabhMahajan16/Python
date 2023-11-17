from hangman_arts import caeser

print(caeser)
print("\n\n\n")
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))
if shift > 255:
    shift=shift-255
new_String=""
endless=True

def encode(message, encodeShift):
    new_message=""
    for letter in message:
        new_value=ord(letter)+encodeShift
        new_message+=chr(new_value)
    print(" \n Here is the result of encoded message below \n\n")
    print(new_message)

def decode(message, decodeShift):
    new_message=""
    for letter in message:
        new_value=ord(letter)-decodeShift
        new_message+=chr(new_value)
    print(" \n Here is the result of decoded message below \n\n")
    print(new_message)
    return new_message



def user_call(call):
    if direction == "encode":
        encode(message=text, encodeShift=shift)
    if direction == "decode":
        decode(message=text, decodeShift=shift)
    
    
    
while endless:
    user_call(direction)
    continue_end=input("\n\n Type yes if 'you' want to go again or 'no' if you want to end \n\n").lower()
    if continue_end == "yes":
        direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        user_call(direction)
    else:
        endless=False