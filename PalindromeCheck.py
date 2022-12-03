import string

# get string from input
str1 = input("Please enter a string\n")
print("\n")
# convert string to lowercase
str2 = str1.lower()
#remove bad characters
bad_chars = string.whitespace + string.punctuation + string.digits
for i in bad_chars:
    str2 = str2.replace(i, '')

print(str2)
# check whether reverse of string is equal the string
str3 = str2[:: -1] # str3 = str2 in reverse

if str2 == str3:
    print("string is a palindrome\n")
else:
    print("String isn't a palindrome\n")

