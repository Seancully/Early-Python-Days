
# function
def length(str):
    counter = 0

    for c in str:
        counter += 1
    
    print("Length of string: ")
    return counter

# main scope
str = input("PLease enter a string\n")
print(length(str))
