# Demonstrate how variables are created and how they work
# Author: Daniel Yang
# Date: 11 April 2025
# version 1.0

# Different type of variebles
# Store a number
my_number = 80 # assigning 80 to my_number (variable)
print(my_number)

my_number2 = 7 # I have reassigned the value of variale
print(my_number2)

# store a string
name_1 = "Daniel"
print(name_1)

# Assign the value of one variable to another
my_number = name_1
print(my_number)# Don't assign values to variable that don't make sense

# creating a new variable
num_1 = 5
num_2 = 17

'''do calculations with variables and the result
in Another variable.'''

sum1 = 5 + 17 # This is not good practice
print (sum)

#better way
sum1 = num_1 + num_2
print(sum1)

sum_string1 = "17" # this stores a string
sum_string2 = "5"

# Adding strings together is called concatenation.
sum = sum_string1 + sum_string2
print(sum)
print(sum1)

print(f"My calculation for {sum_string1} + {sum_string2} = {sum1}")