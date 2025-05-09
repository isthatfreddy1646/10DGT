# Demonstrate how to use while loops and if  statements
# Daniel Yang
# 9 May 2025
# version 1

# while loop
keep_going = "" # The variable contains an empty string
while keep_going == "":

    like_chinesetea =input("Do you like chinese tea")
    
    if like_chinesetea == "yes":
        print("That is great. I like chinese tea too!")
        keep_going = "finished"

    if like_chinesetea == "no":
        print("you are missing out, you should give a try")
        keep_going = "finished"