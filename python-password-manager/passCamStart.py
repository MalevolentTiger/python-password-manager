"""
Built for a capstone project by Cameron Metzger. Some code built using
DivyanshuAG's password manager located at the following link as reference:
https://github.com/DivyanshuAG/Password-Manager-Using-Python
passCamChangeAttribute.py is the same as DivyanshuAG's change_attribute.py 
to easily hide the db folder and .env folder.
"""

from passCamMenu import password_choice, welcome, startup, store, view

if __name__ == '__main__':
    welcome()

    while True:
        question1 = startup()
        if question1 == "1":
            store()
        elif question1 == "2":
            view()
        elif question1 == "3":
            password_choice()
        elif question1 == "4":
            exit()
        else:
            print("-" * 40)
            print("Please enter a valid option.")
            print("-" * 40)