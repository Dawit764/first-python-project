balance = 1000
pin = 1234


def main():
    while True:
        try:
            user_pin = int(input("Enter your 4_digit PIN:")) 
    
            if user_pin == 1234:
                print("\n--- Access Granted ---")
                break
            else:
                print("Access Denied! Try again.")
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue
    while True:
        print(f"Your current balance is: ${balance}")    
        choice = input("Type 'W' to Withdraw or 'D' to Deposit, or 'Q' to quit: ").upper()  
    
        if choice == 'W':
            withdrawal_amount()
        elif choice =='D':
            deposit_amount()
        elif choice =='Q':
            print("Thank you for using our ATM. Goodbye!")
            break
        else:
            print("Invalid Choice.")
        
        
def withdrawal_amount():
    global balance
    amount = float(input("How much? "))
    if amount > balance:
        print("Insufficient Funds.")
    elif amount % 10 != 0:
        print("Error: This ATM only dispenses $10 bills.")
    elif amount <= 0:
        print("Invalid amount!")
    else:
        balance -= amount
        print(f"Dispensing Cash. New balance: ${balance}")
    
        
  

def deposit_amount():
    global balance
    amt = float(input("How much? "))
    if amt > 0:
        balance += amt
        print(f"Deposit successful. New balance: ${balance}")
    else:
        print("Invalid Amount.")

main()
    