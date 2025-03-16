from func import *
from pincode import pincode
from log import log

pincode_check_running = True
pincode_check = False
while pincode_check_running:
    print("*********************")
    enter_pincode = input("Enter PIN-code: ")
    if enter_pincode == pincode[1]:
        print("Correct PIN-code")
        pincode_check_running = False
        pincode_check = True
    else:
        print("Wrong PIN-code")
        pincode_check_running = True
        is_running = False
    print("*********************")

def main():
    balance = 0
    if pincode_check:
        is_running = True

    while is_running:
        print("*********************")
        print("   Banking program   ")
        print("*********************")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change PIN-code")
        print("5. Apply Interest")
        print("6. Show Log")
        print("7. Exit")
        print("*********************")

        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '4':
            switch_pincode(pincode)
        elif choice == '5':
            print("*********************")
            answer = input("Do you want to increase your balance on 5%? (y/n): ").lower()
            if answer == "y":
                balance = balance + (balance * 0.05)
            else:
                continue
        elif choice == '6':
            show_log(log)
        elif choice == '7':
            is_running = False
        else:
            print("*********************")
            print("That is not valid choice")
            print("*********************")
    print("*********************")
    print("Thank you! Have a nice day")
    print("*********************")
if __name__ == '__main__':
    main()