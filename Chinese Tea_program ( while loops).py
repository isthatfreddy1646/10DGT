# Demonstrate how to use while loops and if  statements
# Daniel Yang
# 9 May 2025
# version 1

# while loop
'''keep_going = "" # The variable contains an empty string
while keep_going == "":

    like_chinesetea =input("Do you like chinese tea")
    
    if like_chinesetea == "yes":
        print("That is great. I like chinese tea too!")
        keep_going = "finished"

    if like_chinesetea == "no":
        print("you are missing out, you should give a try")
        keep_going = "finished"
        '''

# version 2. making the program pythonic.
keep_going = "" 
while keep_going == "":
    # .lower converts the answer to lower case
    like_chinesetea = input("Do you like chinese tea?").lower()
    if like_chinesetea == "yes" or like_chinesetea == 'y':
        print("That is great. I like chinese tea too!")

    elif like_chinesetea == "no" or like_chinesetea == "n":
     print("you are missing out")

    like_coffee = input("Do you like coffee instead?").upper()

    if like_coffee == "YES" or like_coffee == "Y":
        print("Good for you. Give chinese tea another try :)")
    elif like_coffee == "NO" or like_coffee == "N":
        print("I am sorry. that is all I have for now")
    else:
        print("I don't understand, please say yes or no")
    
    keep_going = input("Press <enter> to continue or other key to quit")
    