import sqlite3
from passCamEncryption import encryptPassword, decryptPassword
from os.path import dirname, abspath
from os.path import join as path_join

#Database connection
def connect_database():
    try:
        current_dir = dirname(abspath(__file__))
        db_file = path_join(current_dir, 'passCam.db')
        connection = sqlite3.connect(db_file)
    except Exception as e:
        print(e)
    return connection

def create_table():
    tableCreate = """CREATE TABLE IF NOT EXISTS passwords(email BLOB NOT NULL, password BLOB NOT NULL, website TEXT NOT NULL)"""
    connection = connect_database()
    cursor = connection.cursor()
    cursor.execute(tableCreate)
    connection.commit()

def store_data(email, password, website):
    connection = connect_database()
    cursor = connection.cursor()
    password = encryptPassword(password)
    cursor.execute("""INSERT INTO passwords (email, password, website) VALUES (?,?,?)""", (email, password, website))
    connection.commit()

def find_info(email):
    connection = connect_database()
    cursor = connection.cursor()
    search = "SELECT * FROM passwords WHERE email = '{}'".format(email)
    cursor.execute(search)
    row = cursor.fetchone()
    while row:
        user, password, website = row
        print('-' * 40)
        print("Email or Username: ", user)
        print("Wesbite: ", website)
        print('-' * 40)

        question = True
        keepSearching = True

        while question == True:
            print("Would you like to see the password for this account?")
            print("Y/N")
            choice = input(": ")
            if choice.lower() != "y" and choice.lower() != "n" and choice.lower() != "yes" and choice.lower() != "no":
                print("Sorry, that is not y/n")
                print("Please type one of the options.")
            elif choice.lower() == "y" or choice.lower() == "yes":
                unencryptedPassword = decryptPassword(password)
                print("The password for this account is: ", unencryptedPassword)
                question = False
                keepSearching = False
            elif choice.lower() == "n" or choice.lower() == "no":
                question = False
                row = cursor.fetchone()
        
        if keepSearching == False:
            break

    connection.commit()
