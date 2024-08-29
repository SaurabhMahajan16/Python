#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
PLACEHOLDER="[name]"
realNames=[]
def addName(person):
       with open('./Input/Letters/starting_letter.txt', mode='r') as invite:   
           matter=invite.read()
           newMatter=matter.replace(PLACEHOLDER,person)
           createAnInvitation(person,newMatter)
           print(newMatter)

def createAnInvitation(invitee,invite):
    invitationName="./Output/ReadyToSend/"+invitee+".txt"
    print(invitationName)
    with open(file=invitationName, mode='w') as invitation:
        invitation.write(invite)
        
def readNames():
    with open('./Input/Names/invited_names.txt') as file:


                 names= file.readlines()

                 #print(name)
    for person in names:
        name=person.strip('\n')
        #print(name)
        addName(name)
        realNames.append(name)

readNames()


        


    