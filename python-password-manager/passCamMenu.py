from passCamDatabase import create_table, store_data, find_info
from passCamPasswords import generate_normal, generate_custom
from passCamChangeAttribute import change_file_attribute
from passCamEncryption import generateKey, encryptPassword, decryptPassword

def welcome():
    print("-" * 40)
    print("Welcome to PassCam! A work in progress \npassword manager built by Cameron Metzger.")
    print("-" * 40)
    
def startup():
    #Create table
    create_table()
    #Create encryption key
    generateKey()
    #Make sure database and .env files are hidden from view
    change_file_attribute('passCam.db')
    change_file_attribute('.env')
    #Aesthetic menu for ease of use
    print("-" * 40)
    print("What would you like to do?")
    print("1: Store Data")
    print("2: Find Data")
    print("3: Generate Password")
    print("4: Quit")
    print("-" * 40)
    return input(": ")

def store():
    print("-" * 40)
    email = input("Email or Username: ")
    password = input("Password: ")
    website = input("Website: ")
    store_data(email, password, website)
    print("Data has been stored.")

def view():
    print("-" * 40)
    email = input("Email or Username: ")
    find_info(email)

def store_genpass(passwd):
    print("-" * 40)
    email = input("Email or Username: ")
    password = encryptPassword(passwd)
    website = input("Website: ")
    store_data(email, password, website)
    print("Data has been stored.")

def password_choice():
    step = 1
    while step == 1:
        print("-" * 40)
        print("Would you like to customize the characters in the password? ")
        print("y/n")
        choice = input(": ")
        if choice.lower() == "n":
            passwd = generate_normal()
            step2 = 1
            while step2 == 1:
                print("-" * 40)
                print("Would you like to save this password to an account?")
                print("y/n")
                choice2 = input(": ")
                if choice2.lower() == "y":
                    store_genpass(passwd)
                    step = 0
                    step2 = 0
                elif choice2.lower() == "n":
                    step = 0
                    step2 = 0
                else:
                    print("-" * 40)
                    print("Please enter y or n.")
                    print("-" * 40)
        elif choice.lower() == "y":
            passwd = generate_custom()
            step3 = 1
            while step3 == 1:
                print("-" * 40)
                print("Would you like to save this password to an account?")
                print("y/n")
                choice2 = input(": ")
                if choice2.lower() == "y":
                    store_genpass(passwd)
                    step = 0
                    step3 = 0
                elif choice2.lower() == "n":
                    step = 0
                    step3 = 0
                else:
                    print("-" * 40)
                    print("Please enter y or n.")
                    print("-" * 40)
        else:
            print("-" * 40)
            print("This is not a valid option.")
            print("-" * 40)