###########################################################
#  Computer
#
#  This is a password program
#  use the while loop
#    Determine if the user is ready to encrypt or decrypt
#  Statement use the if
#    Set the variable
#    input the key and message
#    for loop to Generate a new string then Encrypt or decrypt
#       If it is encrypted, the message is manipulated in order
#       If it is decryption, look it up in the string in reverse order
#    Output the encrypted or decrypted string
#    Determine whether the user continues
#
###########################################################
answer = input("Would you like to (D)ecrypt, (E)ncrypt or (Q)uit? ")
#It's just the beginning

while (answer.upper()=='E')or(answer.upper()=='D')or(answer.upper()!='Q'):
#End of judgment

    old = "abcdefghijklmnopqrstuvwxyz"
    new = "abcdefghijklmnopqrstuvwxyz"
    add = ""
    new_list = ""
    new_key = ""
    e = ""
    #Initializing variable

    if answer.upper() == 'E':
    #When the input "e"
    
        key = input("Please enter a keyword: ").lower()
        #input keyword
        
        while (key.isalpha() == False) or (len(key) > 26):
        #When input character is greater than 26 or is not all characters.
        
            print("There is an error in the keyword. \
                  It must be all letters and a maximum length of 26")
            key = input("Please enter a keyword: ").lower()
        else:
        #Let's do the first loop
        #Determine that all of the letters in the input key appear only once
        #If there is a repeat
        #delete
        #Use slicing and splicing functions
        #And I'm going to put them in order
            for i in range(0,len(key)):
                if key[i] not in new_key:
                    new_key = new_key + key[i]
                    
            #Let's do the second loop
            #Pairing of strings
            #If the same, then the letter ahead
            #Use slicing and splicing functions
            for j in range(0,len(new_key)):
                same1 = old.find(new_key[j])
                old = old[:same1] + old[same1+1:]
            new_list = new_key + old
            
        message = input("Enter your message: ").lower()
        
        #Let's do the third cycle
        #Enter a cipher
        #The number of loops is the length of the ciphertext
        #Look for the number of digits encrypted
        #Then do the second encryption
        #By affine code
        #Output the letter of this number
        for k in range(0,len(message)):
            if message[k].isalpha() == False:
                e = e + message[k]
            else:
                same2 = new.find(message[k])
                num = (5*same2+8)%26
                e = e + new_list[num]
                
        print("your encoded message: ",e)
        
        answer = input("Would you like to (D)ecrypt, (E)ncrypt or (Q)uit? ")
        
    elif answer.upper() == 'D':
    #When the input "d"
    
        key = input("Please enter a keyword: ").lower()
        #input keyword
        
        while (key.isalpha() == False) or (len(key) > 26):
        #When input character is greater than 26 or is not all characters.
        
            print("There is an error in the keyword. \
                  It must be all letters and a maximum length of 26")
            key = input("Please enter a keyword: ").lower()
        else:
        #Let's do the first loop
        #Determine that all of the letters in the input key appear only once
        #If there is a repeat
        #delete
        #Use slicing and splicing functions
        #And I'm going to put them in order
            for i in range(0,len(key)):
                if key[i] not in new_key:
                    new_key = new_key + key[i]
                    
            #Let's do the second loop
            #Pairing of strings
            #If the same, then the letter ahead
            #Use slicing and splicing functions
            for j in range(0,len(new_key)):
                same1 = old.find(new_key[j])
                old = old[:same1] + old[same1+1:]
            new_list = new_key + old
            
        message = input("Enter your message: ").lower()
        
        #Let's do the third cycle
        #Enter a cipher
        #Arrange all the affine passwords in the new string
        for x in range(0,len(new_list)):
            same3 = new_list.find(new_list[x])
            num = (5*same3+8)%26
            add = add + new_list[num]
            
        #Let's do the fourth cycle
        #Look for ciphertext in the new string
        for k in range(0,len(message)):
            if message[k].isalpha() == False:
                e = e + message[k]
            else:
                same4 = add.find(message[k])
                e = e + new[same4]
        
        print("your decoded message: ",e)
        
        answer = input("Would you like to (D)ecrypt, (E)ncrypt or (Q)uit? ")
        
    elif answer.upper() != 'Q':
    #If you enter illegal characters
        print("ERROR")
        answer = input("Would you like to (D)ecrypt, (E)ncrypt or (Q)uit? ")
        
else:
    print("See you again soon!")
