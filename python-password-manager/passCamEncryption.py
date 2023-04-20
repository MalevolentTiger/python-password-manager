from cryptography.fernet import Fernet
from os.path import exists as file_exists

def generateKey():
    check = file_exists('.env')
    if check == True:
        pass
    elif check == False:
        key = Fernet.generate_key()
        with open(".env", "wb") as keyFile:
            keyFile.write(key)

def loadKey():
    return open(".env", "rb").read()

def encryptPassword(password):
    key = loadKey()
    fernet = Fernet(key)
    encryptedPass = fernet.encrypt(password.encode())
    return encryptedPass

def decryptPassword(password):
    key = loadKey()
    fernet = Fernet(key)
    decryptedPass = fernet.decrypt(password).decode()
    return decryptedPass

    
#key = Fernet.generate_key()
#fernet = Fernet(key)
#password = "testPass1"
#encryptPassword = fernet.encrypt(password.encode())
#print("original password: ", password)
#print("encrypted password: ", encryptPassword)
#decryptPassword = fernet.decrypt(encryptPassword).decode()
#print("decrypted password: ", decryptPassword)