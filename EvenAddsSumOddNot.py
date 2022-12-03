sum = 0

while True:

    number = (input("Please enter a number or '.' to leave: "))

    # for ending program
    if number == '.':
        break

    # checks if user input is even or odd (adds to sum if even)
    if int(number) % 2 == 0:
        sum += int(number)
        continue # quite literally just means continue
    else:
        print("Only even numbers allowed")
        continue

# prints sum once '.' is entered    
print("Sum: ", sum)