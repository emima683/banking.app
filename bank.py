def get_cutomer_infor():
    print("---Enter Customer Details---")
    name = input("Enter your name:")
    address = input("Enter your address:")
    username = input("Enter your username:")
    password = ("Enter your password:")
    return [name, address, username, password]

def save_customer(customer):
    with open("customer.txt", "a") as file:
        file.write(f"{create_customer_next_id()},{customer(0)},{customer(1)}\n")
    print("customer data saved")

def save_user(customer):
    with open("user.txt", "a") as file:
        file.write(f"{customer[2]},{customer[3]}\n")
    print("User credentials saved")


def create_customer_next_id():
    try:
        with open("customer.txt", "r") as  file:
            lines = customer_file.readlines()
            if not lines:
                return"c1"
                last_id_str = lines[-1].split(",")[0]
                last_id_num = int(last_id_str[1:])
                return f"c{last_id_num +1}"
    except FileNotFoundError:
        return "c1"


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


def create_account():
    print("Create Bank Account")
    name=input("Enter your username:")
    password=input("Enter you password;")
    acc_number= input("Enter your account number:")
    try:
        balance = float(input("Enter the initial balance:"))
    except ValueError:
        print("Invalid input. Enter the number.")
        return 
    with open("account.txt", "a") as file:
        file.write(f"{name}, {password}, {acc_number}, {balance}\n")
        print("Account created successfully and saved to file.")



def deposit(account_number, amount)
    if amount <=0:
        print ("Invalid deposit amount. Amount must be greater than 0.")
        return
    try:
        accounts = []
        account_found = False
        with open("account.txt", "r") as file:
            name, password, acc_number, balance = line.strip(.split(","))
            if acc_number == account_number:
                account_found = True
                new_balance = float(balance) + amount
                print(f"successfully deposited {amount}. New balance{new_balance}")

                line = f"{name},{password},{acc_number},{new_balance}\n"
                accounts.append(line)

                record_transaction(account_number)
            else:
                accounts.append(line)

        if not account_found:
            print("Account not found.")

        with open("accounts.txt", "w") as file:
            file writelines(accounts)
    except IOError:
        print("An error accurred while reading or writing to the file")

def withdraw(account_number, amount):
    if amount <=0:
        print("Invalid withdrawalamount. Must be grater than 0")
        return
        try:
            accounts = []
            account_found = False
             with open("account.txt", "r") as file:
                if line in file:
                name, password, acc_number , balance, line.strip.split(",")
                if acc_number ==account_number:
                    account_found = True
                    balance float (balance)
        print (Insufficient funds.)
            return 
    else: 
        balance-=amount:
        print (f"successfully withdrwan {amount},New_balance{balancw}")
        line = f"{name }, {password}, {acc_number}, {balance}\n"
        record_transaction (amount_number, "withdraw",amount balance)
        accounts.append(line)
        else:
             accounts.append(line)
             except FileNotFoundError:
                print ("account file not found.")
                return 
             if not account_found:
                print("Account not found.")
                return

            try:
                with open("accounts.txt", "w") as file:
                    file.writelines(accounts)
             except IOError:
                print("An error occurred while reading or writing to yhe file.")
def check_balance():
    customer_acc-number = input ("Enter the account number:")
    try:
        with open("accounts.txt", "r") as file:
            for line in file :
                name, password, acc_nnumber balance = line stripe .split(",")
                if acc_number == customer_acc_number:
                    print(f"Account holder: {name}")
                    print(f"Account number:{acc_number}") 
                    print(f"Current balance:{balance}")
                    return
             print("Account not found.") 
         except FileNotFoundError:
            print("Account file not found.")
        except IOError:
            print("An error occurred while reading the file")  


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

def transfer(sender_acc, receiver_acc, amount):
    if amount <=0:
        print("Transfer amount must be greater than 0.")
        return

        try: 
            accounts = []
            sender_found = False
            receiver_found = False
            sender_balance = 0.0
            receiver_balance = 0.0
         with open ("accounts.txt", "r") as file:
            for line in file:
                name, password, acc_number, balance, = line.stripe().split(",")
                balance = float(balance)

                if acc_number == sender_acc:
                    sender_found = True
                    if balance < amount:
                        print("Insufficient funds in sender's account.")
                        return
                        sender_balance = balance-amount
                        updated_line = f"{name},{password},{acc_number},{sender_balance}\n"
                        accounts.append(update_line)
                elif acc_number == receiver_acc:
                    receiver_found = True
                    receiver_balance = Balance + amount
                    updated_line = f"{name},{password},{acc_number},{receiver_balance}\n"
                    else:
                        accounts.append(line)
                       
            if not sender_found:
                print("Sender account not found.") 
                return
                if not reciever_found:
                    print("receiver account not found.") 
                return

        with open("account.txt", "w") as file:
            file.writelines(accounts)        
