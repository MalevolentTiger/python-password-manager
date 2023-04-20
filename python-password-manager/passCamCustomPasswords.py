import random
import string

def length_of_pass():
    print("How long of a password would you like generated?")
    return input("Length: ")

def lowercase():
    print("Would you like lowercase letters?")
    print("y/n?")
    return input(": ")

def uppercase():
    print("Would you like uppercase letters?")
    print("y/n?")
    return input(": ")

def numbers():
    print("Would you like numbers letters?")
    print("y/n?")
    return input(": ")

def punctuation():
    print("Would you like special characters?")
    print("y/n")
    return input(": ")