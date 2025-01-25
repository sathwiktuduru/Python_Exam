def check_balance(balance):
    #prints the account balance
    print(f"Current balance: {balance}") 
    return balance

def deposit(balance):
    deposit_amount=int(input("Enter the amount: ")) #taking the deposit amount from the use
    balance=balance+deposit_amount #Adding the deposited amount to the balance
    print(f"Currect balance after deposit: {balance}") 
    return balance

def withdraw(balance):
    #money is withdrawn if balance is available, if not it shows insufficient balance
    withdraw_amount=int(input("Enter withdraw amount: "))
    if(withdraw_amount>balance):
        print("Insufficient Balance")
    else:
        balance=balance-withdraw_amount
        print(f"Balance after withdraw: {balance}")
    return balance

def main():
    #taking the required inputs from the user to make the process
    balance=0
    while True:
        print("Enter 1 to check balance")
        print("Enter 2 to deposit")
        print("Enter 3 to withdraw")
        print("Enter 4 to Exit")
        choice=int(input())
        if choice == 4:
            break
        elif choice == 1:
            amount=check_balance(balance)
            balance=amount
        elif choice == 2:
            balance=deposit(balance)
        elif choice == 3:
            balance=withdraw(balance)
main()