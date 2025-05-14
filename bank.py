import os

def get_customer_info():
    print("---Enter Customer Details---")
    name = input("Enter your name:")
    address = input("Enter your address:")
    username = input("Enter your username:")
    password = input("Enter your password:")
    return [name, address, username, password]

def save_customer(customer):
    with open("customer.txt", "a") as file:
        file.write(f"{create_customer_next_id()},{customer[0]},{customer[1]}\n")
    print("customer data saved")

def save_user(customer):
    with open("user.txt", "a") as file:
        file.write(f"{customer[2]},{customer[3]}\n")
    print("User credentials saved")

#Generate the next customer ID......................................................



def create_customer_next_id():
    try:
        with open("customer.txt", "r") as customer_file:
            lines = customer_file.readlines()
            if not lines:
                return"c1"
            last_id_str = lines[-1].split(",")[0]
            last_id_num = int(last_id_str[1:])
            return f"c{last_id_num +1}"
    except FileNotFoundError:
        return "c1"

#user login check...................................................................

def user_login():
    username=input("Enter your username:")
    password=input("Enter your password:")
    try:
        with open("user.txt","r") as file:
            for line in file:
                user,pwd = line.strip().split(",")
                if user==username and pwd==password:
                    print("Login Successful.")
                    return True
    except FileNotFoundError:
        pass
    print("Invalid username or password.")
    return False

#Create a bank account..............................................................

def create_account():
    print("Create Bank Account")
    name = input("Enter your username:")
    password = input("Enter you password:")
    acc_number = input("Enter your account number:").strip()
    try:
        balance = int(input("Enter the initial balance:"))
    except ValueError:
        print("Invalid input. Enter the number.")
        return 
    with open("accounts.txt", "a") as file:
        file.write(f"{name}, {password}, {acc_number}, {balance},\n")
        print("Account created successfully and saved to file.")

#Deposit.............................................................................
def deposit(account_number, amount):
    if amount <= 0:
        print("Invalid deposit amount. Amount must be greater than 0.")
        return
    try:
        account_found = 0
        fill=open("accounts.txt", "r")
        data=fill.readlines()
        fill.close()
        for i in data:
            m=i.split(",")
            if int(m[2])==int(account_number):
                data.remove(i)
                gg=m[3]
                m[3]=int(gg)+int(amount)
                account_found=10
            else:
                pass
        fill=open("accounts.txt", "w")
        fill.writelines(data)
        fill.close()
        fill=open("accounts.txt", "a")
        fill.write(f"{m[0]},{m[1]},{m[2]},{m[3]},\n")
        fill.close()
        if  account_found==0:
            print("Account not found.")
        else:
            pass
    except IOError:
        print("An error accurred while reading or writing to the file")

#Withdraw............................................................................

def withdraw(account_number, amount):
    if amount <= 0:
        print("Invalid deposit amount. Amount must be greater than 0.")
        return
    else:
        try:
            account_found = 0
            fill=open("accounts.txt", "r")
            data=fill.readlines()
            fill.close()
            for i in data:
                m=i.split(",")
                if int(m[2])==int(account_number):
                    data.remove(i)
                    gg=m[3]
                    if int(gg)<int(amount):
                        print("invalid acount balance")
                        return
                    else:
                        m[3]=int(gg)-int(amount)
                        account_found=10
                        fill=open("accounts.txt", "w")
                        fill.writelines(data)
                        fill.close()
                        fill=open("accounts.txt", "a")
                        fill.write(f"{m[0]},{m[1]},{m[2]},{m[3]},\n")
                        fill.close()
                        return
                else:
                    pass
            
            if  account_found==0:
                print("Account not found.")
            else:
                pass
        except IOError:
            print("An error accurred while reading or writing to the file")

#.................................................

def check_balance():
    customer_acc_number = input ("Enter the account number:")
    try:
         
        fill=open("accounts.txt", "r")
        data=fill.readlines()
        fill.close()
        for i in data:
            m=i.split(",")
            if int(m[2])==int(customer_acc_number):
                print(f"{m[3]}")
            else:
                pass
    except FileNotFoundError:
            print("Accounts file not found.")
    except IOError:
            print("An error occurred while reading the file.")  

#Transaction history........................................................................

def record_transaction(account_number, transaction_type, amount, new_balance):
    
    try:
        with open("Transaction.txt", "a") as file:
            file.write(f"{account_number},{transaction_type},{amount},{new_balance}\n")
    except IOError:
        print("Error occurred while writing the transaction history")


def display_transaction_history(account_number):
    try:
        with open("transaction.txt", "r") as file:
            print("\n---Trasaction History---")
            print("{:<12} {:<10} {:<12}".format("Type","Amount","Balance"))
            print("-" *30)
            found = False
            for line in file:
                data = line.strip().split(",")
                if data[0] == account_number:
                    print("{:<12} {:<10} {:<12}".format (data[1], data[2], data[3]))
                    found = True
            if not found:
                print("No transaction found for this account.")
    except FileNotFoundError:
        print("Transaction file not found.")
    except IOError:
        print("Error occurred whiloe reading the transaction history.")


#Main user menu.................................................................................

def user_registration():
    while True:
        print("\n---- Welcome to Mini Banking System----")
        print("1. Register User")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice(1-3):")

        if choice == "1":
            customer = get_customer_info()
            if customer:
                save_customer(customer)
                save_user(customer)

        elif choice == "2":
            if user_login ():
                while True:
                    print("\n--- Main Menu ---")
                    print("1. Create Bank Account")
                    print("2. Deposit Money")
                    print("3. Withdraw Money")
                    print("4. Check Balance")
                    print("5. Transaction History")
                    print("6. Logout")
                    choice = input("Enter your choice (1-7):")


                    if choice == "1":
                        create_account()
                    elif choice == "2":
                        acc = input("Enter account number:")
                        #try:
                        amt = int(input("Enter deposit amount:"))
                        deposit(acc, amt)
                        # except ValueError:
                        #     print("Invalid amount.")
                    elif choice == "3":
                        acc = input("Enter account number")
                        try:
                            amt = float(input("Enter withdrawal amount:"))
                            withdraw(acc, amt)
                        except ValueError:
                            print("Invalid amount.")
                    elif choice == "4":
                        check_balance()
                    elif choice == "5":
                        acc = input("Enter account number:")
                        display_transaction_history(acc)
                    
                    elif choice == "6":
                        print("Logged out.")
                        break
                    else:
                        print("Invalid option.")

        elif choice == "3":
            print("Thank you for using Mini Banking System. Have a Nice Day.")
            break
        else:
            print("Invalid choice. Try again.")


user_registration()



            







