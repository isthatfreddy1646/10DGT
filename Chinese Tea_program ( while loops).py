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

'''# version 2. making the program pythonic.
keep_going = "" 
while keep_going == "":
    # .lower converts the answer to lower case
    like_chinesetea = input("Do you like chinese tea?").lower()
    if like_chinesetea == "yes" or like_chinesetea == 'y':
        print("That is great. I like chinese tea too!")
        keep_going = 'STOP'

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
    '''
'''#version 3.0
# Create a function that I can use over and over again.
# Make my code recyeclable.
# The program will ask a person for a number an ddo something with it.
# Loop the program until a valid number gets entered.

def intcheck(): # def creates a function. intcheck is the function name.
    valid = False
    while not valid:
        error = "whoops, you have enter the wrong number. Please " \
        "enter a valid integer between 1 to 10."

        try:
            response = int(input("Enter and integer between 1 and 10: "))
           

            if response >=1 and response <=10:
                print(response)
                valid = True
            else:
                print(error)
        
        
        except:
            print(error)

intcheck() # To call(use) the function, write out it's name'''

#version 3.0
# Create a function that I can use over and over again.
# Make my code recyeclable.
# The program will ask a person for a number an ddo something with it.
# Loop the program until a valid number gets entered.

def intcheck(question, low, high): # def creates a function. intcheck is the function name.
    valid = False
    while not valid:
        error = f"whoops, you have enter the wrong number. Please " \
        f"enter a valid integer between {low} and {high} ."

        try:
            response = int(input(f"Enter and integer between {low} and {high}: "))
           

            if low <= response <= high:
                print(f"you have entered {response}")
                valid = True
            else:
                print(error)
        
        
        except ValueError:
            print(error)
    return response

num1 = intcheck("Enter a number between 1 and 10",1, 10) # To call(use) the function, write out it's name.
num2 = intcheck("Enter a number between 15 and 20", 15,20 )
# print(num1) # used to check for correct storage.
#adding the responses together
sum_num = num1 + num2

# multiply the responses
multiply = num1 * num2

print(f"Your two numbers added together are {sum_num}.\n")
print(f"your two numbers multiply result in {multiply}.")