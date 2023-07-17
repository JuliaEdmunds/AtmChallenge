import atm

# (2 hour challenge - python)
# code a function that takes a whole number (int) and a list of currencies denominations
# (also int) and how many of each are available. It should print out how many of each denomination it should give to
# make the provided number (like an atm choosing which banknotes to give out). It should aim to use as few notes as
# possible and print ERROR if it's not possible with the given denominations. The types of denominations and number
# of each available should be variable.
#
# [Stretch] separate into two functions. One that initialises the denominations
# available and one that can Withdraw(int amount). If the withdrawal is successful (meaning there's sufficient notes
# to do it), those notes are removed. Meaning that you can setup an initial amount of cash in the atm and call
# Withdraw with different amounts each time until there's no money left

# Initialize the atm with the banknotes
# Let user either withdraw money or add money to the atm

choosing_operation = True
withdraw_operation = 1
add_money_operation = 2

while choosing_operation:
    operation_type = input(
        f"Hello! If you would like to withdraw money press {withdraw_operation} and if you would like "
        f"to add money to the atm press {add_money_operation} ")
    try:
        operation_type = int(operation_type)
    except ValueError:
        print("This is not a valid number...")
        continue

    if operation_type == withdraw_operation:
        money_from_atm = atm.withdraw_money()
        print(money_from_atm)
        choosing_operation = False

    elif operation_type == add_money_operation:
        current_operation = add_money_operation
        choosing_operation = False

    else:
        print(f"{operation_type} in not a valid operation number.")
        continue
