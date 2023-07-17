import helper

# code a function that takes a whole number (int) and a list of currencies denominations
# (also int) and how many of each are available. It should print out how many of each denomination it should give to
# make the provided number (like an atm choosing which banknotes to give out). It should aim to use as few notes as
# possible and print ERROR if it's not possible with the given denominations. The types of denominations and number
# of each available should be variable.

# Format x$ - amount of notes
money_in_atm = {
    5: 10,
    10: 10,
    20: 10,
    50: 5,
    100: 5,
    200: 1,
    500: 1
}


def check_amount():
    while True:
        amount_to_withdraw = input("How much money would you like to withdraw? ")
        try:
            amount_to_withdraw = int(amount_to_withdraw)
        except ValueError:
            print("This is not a valid number...")
            continue

        else:
            return amount_to_withdraw


def try_withdraw(number, notes_in_atm):
    withdrawn_banknotes = {}
    for banknote in notes_in_atm:
        if number >= banknote:
            if banknote in withdrawn_banknotes:
                withdrawn_banknotes[banknote] += 1
            else:
                withdrawn_banknotes[banknote] = 1

            number = number - banknote

        if number == 0:
            return f"Here is your money: {withdrawn_banknotes}"

    return


def withdraw_from_atm(number, banknotes_in_atm):
    # Sort the dictionary by key in descending order
    ordered_banknotes = dict(sorted(banknotes_in_atm.items(), reverse=True))
    list_of_atm_banknotes = []
    list_of_withdrawn_banknotes = {}

    # Create a list of all notes atm has
    for note in ordered_banknotes:
        number_of_notes = ordered_banknotes[note]
        for banknote in range(number_of_notes):
            list_of_atm_banknotes.append(note)

    # check how many of each denomination to give
    # go combination by combination starting from highest nominals
    # if impossible to make out the amount print "ERROR"

    cloned_list = helper.clone(list_of_atm_banknotes)
    try_withdraw(number, cloned_list)

    for banknote in list_of_atm_banknotes:
        if number >= banknote:
            cloned_list = helper.clone(list_of_atm_banknotes)
            outcome = try_withdraw(number, cloned_list)
            if banknote in list_of_withdrawn_banknotes:
                list_of_withdrawn_banknotes[banknote] += 1
            else:
                list_of_withdrawn_banknotes[banknote] = 1

            number = number - banknote

        if number == 0:
            return f"Here is your money: {list_of_withdrawn_banknotes}"

    return "ERROR"


def withdraw_money():
    amount = check_amount()
    return withdraw_from_atm(amount, money_in_atm)

# [Stretch] separate into two functions. One that initialises the denominations
# available and one that can Withdraw(int amount). If the withdrawal is successful (meaning there's sufficient notes
# to do it), those notes are removed. Meaning that you can setup an initial amount of cash in the atm and call
# Withdraw with different amounts each time until there's no money left
# TODO: include the stretch goal


def add_money():
    # Check how many of what notes to add
    print()
