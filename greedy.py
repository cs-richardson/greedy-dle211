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

# Calculates the number of dimes owed.
dimes = change // 10
change = change % 10

# Calculates the number of nickels owed.
nickels = change // 5
change = change % 5

# Turns the rest of the change into pennies.
pennies = change

# Calculates all the coins required
coins = quarters + dimes + nickels + pennies

# Prints the total amount of coins, and specify the type of coins
print("You owe", coins, "coins, which are:")
if quarters >= 1:
    print(quarters, "quarter(s)")
if dimes >= 1:
    print(dimes, "dime(s)")
if nickels >= 1:
    print(nickels, "nickel(s)")
if pennies == 1:
    print("1 penny")
elif pennies > 1:
    print(pennies, "pennies")
