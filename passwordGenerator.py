#alphabets=[]
#
#alphabets=input().split()
#print(alphabets)
#print(alphabets)
import string
import random
 
# Randomly choose a letter from all the ascii_letters
#randomLetter = random.choice(string.ascii_letters)
#print(string.ascii_uppercase)
##print(randomLetter)
specialChar=['!', '@', '#', '$', '%', '^', '&', '*']
print(type(specialChar))
print("\n\n -----------------------Welcome to password generator ---------------------------\n\n")
passwordLength=int(input("\n length of your password!! \n"))
lowercaseAlphabets=int(input("number of lower case alphabets you want in your password!! \n"))
uppercaseAlphabets=int(input("\n number of upper case alphabets you want in your password!! \n"))
numericCharacters=int(input("\n number of numeric charcters you want in your password!! \n"))
specialCharacters=int(input("\n number of special charcters you want in your password!! \n"))


password=""
if passwordLength==lowercaseAlphabets+uppercaseAlphabets+numericCharacters+specialCharacters:
    #lowercase
    for char in range(0,lowercaseAlphabets):
        password+=random.choice(string.ascii_lowercase)
    #uppercase
    for char in range(0,uppercaseAlphabets):
        password+=random.choice(string.ascii_uppercase)
    #special char
    for char in range(0,specialCharacters):
        password+=random.choice(specialChar)
    #numbers
    for char in range(0, numericCharacters):
        password+=str(random.choice(string.digits))
    print(f"\n your password is below \n {password}\n\n")
else:
    print(f"length of password didnt match with length of characters you enter, please retry!!!")

passwordgenerator=[string.ascii_lowercase]+[string.ascii_uppercase]+specialChar+[string.digits]
generatedString=''.join(random.choices(passwordgenerator, k=passwordLength))

#password="".join(random.choices(passwordgenerator, passwordLength))
print(f"\n\n password is {generatedString} \n\n\n")
