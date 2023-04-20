import sqlite3
from passCamEncryption import encryptPassword, decryptPassword

#Database connection
def connect_database():
    try:
        connection = sqlite3.connect('passCam.db')
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
    cursor.execute("""INSERT INTO passwords (email, password, website) VALUES (?,?,?)""", (email, password, website))
    connection.commit()

def find_info(email):
    connection = connect_database()
    cursor = connection.cursor()
    search = "SELECT * FROM passwords WHERE email = '{}'".format(email)
    cursor.execute(search)
    userEmail = 0
    for row in cursor:
        user, password, website = row
        print('-' * 40)
        print("Email or Username: ", user)
        print("Encrypted Password: ", password)
        print("Website: ", website)
        print('-' * 40)
        userEmail = 1
    while userEmail == 1:
        print("Would you like to view the password for this account?")
        print("Y/N")
        choice = input(": ")
        if choice.lower() == "y":
            password = decryptPassword(password)
            print("Decrypted Password: ", password)
            userEmail = 0
        elif choice.lower() == "n":
            userEmail = 0
        else:
            print("Please enter y or n.")
    connection.commit()
