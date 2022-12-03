# Write a three-line program that prompts for a number, \
# converts the input to an integer, \
# and prints a 0 when the number is even and a 1 when the number is odd.

# user input
number = input('Enter a whole number:\n')
number = int(number) 

if number % 2 == 0:
    print('Number is even')
else:
    print('Number is odd')



