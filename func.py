from log import log

def show_balance(balance):
    print("*********************")
    print(f"Your balnce is ${balance:.2f}")
    print("*********************")
    log.append("show_balance")

def switch_pincode(pincode):
    pincode_swap_running = True
    while pincode_swap_running:
        print("*********************")
        print(f"Your PIN-code is {pincode[1]}")
        print("*********************")
        new_pincode = input("Enter your new PIN-code: ")
        pincode[1] = new_pincode
        log.append(f"switch_pincode {new_pincode}")
        return pincode

def deposit():
    print("*********************")
    amount = float(input("Enter an amount to be deposited: "))
    print("*********************")

    if amount < 0:
        print("That's not a valid amount")
        return 0
    else:
        log.append(f"deposit {amount}")
        return amount

def withdraw(balance):
    print("*********************")
    amount = float(input("Enter amount to be withdrawn: "))
    print("*********************")

    if amount > 500:
        print("*********************")
        print("You can't withdraw more than 500$")
        print("*********************")
        log.append(f"can't_withdraw_more_500")
        return 0

    elif amount > balance:
        print("*********************")
        print("Insufficient funds")
        print("*********************")
        log.append(f"withdraw_insufficient_funds")
        return 0

    elif amount < 0:
        print("*********************")
        print("Amount must be greater than 0")
        print("*********************")
        return 0
    else:
        log.append(f"withdraw {amount}")
        return amount

def show_log(log):
    print("*********************")
    print("Bank log")
    for i, l in enumerate(log, 1):
        print(f"{i} {l}")
    print("*********************")
    log.append("show_log")
    return 0