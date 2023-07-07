from cryptography.fernet import Fernet
from os.path import dirname, abspath
from os.path import join as path_join
from os.path import exists

def generateKey():
    current_dir = dirname(abspath(__file__))
    env_file_path = path_join(current_dir, ".env")

    if not exists(env_file_path):
        key = Fernet.generate_key()
        with open(env_file_path, "wb") as keyFile:
            keyFile.write(key)

def loadKey():
    current_dir = dirname(abspath(__file__))
    env_file_path = path_join(current_dir, ".env")
    return open(env_file_path, "rb").read()

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