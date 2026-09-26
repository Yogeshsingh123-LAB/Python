import random
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1
rowa = 3
columns = 3
symbols_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

def get_slot_machine_spin(rows, cols, symbols):
    pass

def deposit():
    while True:
        amount = input("Enter the amount you want to bet $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("amount must be greater than 0")
        else:
            print("please choose interger as an amount")
    return amount
def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES})? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Please enter a number between 1 and {MAX_LINES}.")
        else:
            print("Please enter a valid number.")

    return lines
def get_bet():
    while True:
        amount = input(f"Enter the bet amount per line (${MIN_BET}-${MAX_BET}): $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a valid number.")
    return amount


def main():
    amount = deposit()
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet <= amount:
            break
        else:
            print(f"Total bet (${total_bet}) cannot exceed your deposit (${amount}).")
    print(f"You are bettting ${bet} on {lines} line(s).\nTotal bet is equal to: ${total_bet}")

if __name__ == "__main__":
    main()