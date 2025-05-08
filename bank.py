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








