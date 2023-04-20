import random
import string
from passCamCustomPasswords import length_of_pass, lowercase, uppercase, punctuation, numbers

def generate_normal():
    characters = string.ascii_letters + string.digits + string.punctuation
    passwd = (''.join(random.choice(characters) for i in range(10))) 
    print(passwd)
    return passwd

def generate_custom():
    characters = ""
    step = 1
    while step == 1:
        question1 = lowercase()
        if question1.lower() == "y":
            characters = characters + string.ascii_lowercase
            step = 2
        elif question1.lower() == "n":
            step = 2
        else:
            print("Please enter y or n.")
    while step == 2:
        question2 = uppercase()
        if question2.lower() == "y":
            characters = characters + string.ascii_uppercase
            step = 3
        elif question2.lower() == "n":
            step = 3
        else:
            print("Please enter y or n.")
    while step == 3:
        question3 = numbers()
        if question3.lower() == "y":
            characters = characters + string.digits
            step = 4
        elif question3.lower() == "n":
            step = 4
        else:
            print("Please enter y or n.")
    while step == 4:
        question4 = punctuation()
        if question4.lower() == "y":
            characters = characters + string.punctuation
            step = 5
        elif question4.lower() == "n":
            step = 5
        else:
            print("Please enter y or n.")
    while step == 5:
        question5 = length_of_pass()
        if question5.isdigit() > 0:
            passwd = (''.join(random.choice(characters) for i in range(int(question5))))
            print(passwd)
            step = 0
            return passwd
        elif question5.isdigit() == 0:
            print("Please input a value higher than 0.")
        else:
            print("Please input a numerical value.")