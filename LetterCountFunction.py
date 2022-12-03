import string


def letter_count(str):
    """Function counts only the letters in a string"""

    counter = 0
    for c in str:
        if c.lower() in string.ascii_lowercase:
            counter += 1

    return counter

str = input("Please enter a string to check how many (only) letters it contains: \n")
print(letter_count(str))