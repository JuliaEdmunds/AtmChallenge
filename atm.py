# code a function that takes a whole number (int) and a list of currencies denominations
# (also int) and how many of each are available. It should print out how many of each denomination it should give to
# make the provided number (like an atm choosing which banknotes to give out). It should aim to use as few notes as
# possible and print ERROR if it's not possible with the given denominations. The types of denominations and number
# of each available should be variable.

# [Stretch] separate into two functions. One that initialises the denominations
# available and one that can Withdraw(int amount). If the withdrawal is successful (meaning there's sufficient notes
# to do it), those notes are removed. Meaning that you can setup an initial amount of cash in the atm and call
# Withdraw with different amounts each time until there's no money left

class Atm:
    # Format x$ - amount of notes
    money_in_atm = {
        5: 1,
        20: 3,
        50: 2,
        100: 1,
    }

    def add_money(self, money_to_add):
        for banknote in money_to_add:
            if banknote in self.money_in_atm:
                self.money_in_atm[banknote] += 1
            else:
                self.money_in_atm[banknote] = 1

    def remove_money(self, money_to_remove):
        for banknote in money_to_remove:
            self.money_in_atm[banknote] -= 1
            if self.money_in_atm[banknote] == 0:
                self.money_in_atm.pop(banknote)


class State:
    def __init__(self, remaining, used):
        self.remaining = remaining
        self.used = used

    def __str__(self):
        return f"Remaining: {self.remaining}, used: {self.used}"

    def used_sum(self):
        return sum(self.used)

    def remaining_sum(self):
        return sum(self.remaining)

    def clone(self):
        return State(self.remaining.copy(), self.used.copy())


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


def get_amount():
    while True:
        amount_to_add = input("How much money would you like to add to the atm? Please provide only whole numbers ("
                              "without decimals) and separate the banknotes with commas [,]. ")

        money_to_add_string = amount_to_add.split(",")
        money_to_add = []

        for num in money_to_add_string:
            try:
                current_note = int(num)
                money_to_add.append(current_note)
            except ValueError:
                money_to_add.clear()
                print("This is not a valid format...")
                break
        if all(isinstance(item, int) for item in money_to_add) and money_to_add:
            return money_to_add
        else:
            continue


def remove_same_nominals(self, note):
    # remove all occurrences of the banknote
    updated_list = [i for i in self if i != note]

    return updated_list


def try_withdraw_from_atm(number):
    # Create a list of all notes atm has
    atm = Atm()

    list_of_atm_banknotes = []
    for note in atm.money_in_atm:
        number_of_notes = atm.money_in_atm[note]
        for banknote in range(number_of_notes):
            list_of_atm_banknotes.append(note)

    list_of_atm_banknotes.sort(reverse=True)

    # Add initial State to the checklist
    states_to_check = []
    first_state_used = []
    initial_state = State(list_of_atm_banknotes.copy(), first_state_used.copy())
    states_to_check.append(initial_state)

    while states_to_check:
        current_state = states_to_check[0]
        states_to_check.remove(current_state)
        if current_state.used_sum() == number:
            # With successful withdrawal remove money from atm
            money_to_withdraw = current_state.used
            atm.remove_money(money_to_withdraw)
            return money_to_withdraw
        else:
            # Generate all valid children states and add to the checklist
            while current_state.remaining:
                banknote = current_state.remaining[0]
                if number < banknote:
                    current_state.remaining = remove_same_nominals(current_state.remaining, banknote)
                else:
                    new_state = current_state.clone()
                    new_state.remaining.remove(banknote)
                    new_state.used.append(banknote)
                    # State is only valid if the sum did not go over the number and there is enough remaining to still
                    # make the number
                    remaining_to_withdraw = number - new_state.used_sum()
                    if 0 <= remaining_to_withdraw <= new_state.remaining_sum():
                        states_to_check.append(new_state)
                    # After checking validity remove current variant of note from the state
                    current_state.remaining = remove_same_nominals(current_state.remaining, banknote)

    return "ERROR"


def add_money_to_atm(money_to_add):
    atm = Atm()
    atm.add_money(money_to_add)


def withdraw_money():
    amount = check_amount()
    return try_withdraw_from_atm(amount)


def add_money():
    amount = get_amount()
    add_money_to_atm(amount)
    print(f"Total of {sum(amount)} added to the atm.")
