"""
This program will calculate how much change is owed in coins, based on the
user's input.
Coded by Justin Le, help from Stack Overflow
"""

# Asks the user for a positive float, and then converts it into cents.
while True:
    try:
        change = float(input("How much change is owed? $"))
        if change < 0:
            print("That's not a valid input.")
            continue
        break
    except ValueError:
        print("That's not a valid input.")
change = round(change * 100)

# Calculates the number of quarters owed.
quarters = change // 25
change = change % 25
# If at least 1 quarter is owed, print the number of quarters owed.
if quarters >= 1:
    print("You owe", quarters, "quarter(s).")

# Calculates the number of dimes owed.
dimes = change // 10
change = change % 10
# If at least 1 dime is owed, print the number of dimes owed.
if dimes >= 1:
    print("You owe", dimes, "dime(s).")

# Calculates the number of nickels owed.
nickels = change // 5
change = change % 5
# If at least 1 nickel is owed, print the number of nickels owed.
if nickels == 1:
    print("You owe", nickels, "nickel(s).")

# Turns the rest of the change into pennies.
pennies = change
# If at least 1 pennie is owed, print the number of pennies owed.
if pennies == 1:
    print("You owe 1 penny.")
elif pennies > 1:
    print("You owe", pennies, "pennies.")
