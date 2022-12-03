def even_or_odd(number):
    """A function that will return "even" or "odd" depending on the number"""
    if number % 2 == 0:
        return "even"
    else:
        return "odd"


num = int(input("Enter a number to see if even or odd\n"))
print(even_or_odd(num))