MAX_LINES = 3

def deposit():
    while True:
        # amount = int(input("Deposit amount? $"))
        amount = input("Deposit amount? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Invalid amount!")
        else:
            print("Invalid Entry!")            
        # return amount
    return amount
# deposit()

def get_lines():
    while True:
        lines = input("Enter number of lines (1-" + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Entry 'MUST' be between 1 and {str(MAX_LINES)}!")
        else:
            print("Invalid Entry!")            
    return lines

def get_bet():
    while True:
        lines = input("Enter number of lines (1-" + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Entry 'MUST' be between 1 and {str(MAX_LINES)}!")
        else:
            print("Invalid Entry!")            
    return lines


def main():
    ...
    # balance = deposit()
    # lines = get_lines()
    # print(balance, lines)
# main()

def devide(a, b):
    try:
        a, b = b, a
        return a/b
    except:
        print("Error")
print(devide(10, 0))
