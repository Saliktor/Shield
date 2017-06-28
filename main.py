import os
import encryption

def getUserChoice() -> int:
    exit = False
    valid_options = [1,2]

    while(exit == False):
        print("Enter one of the following values to continue:")
        print("1: Add new information to be encrypted")
        print("2: View encrypted data")
        user_input = input("Enter here: ")

        try:
            user_input = int(user_input)
            if (user_input not in valid_options):
                raise Exception

        except Exception:
            print("Option entered is not valid")
            os.system('cls')

        else:
            return user_input

def storeEncryption(enc:str) -> None:
    file = open("text.txt", 'a', encoding="utf-8")
    file.write(enc)
    file.write(chr(127))
    file.close()


def getTextFromUser() -> None:
    return input("Enter message: ")

def printOutFile(key: str) -> None:
    with open('text.txt') as file:
        text = file.read()

    line = ""
    for c in text:
        if c != chr(127):
            line += c
        else:
            print(encryption.decrypt(key, line))
            line = ""


def handleChoice(key:str, choice:int) -> None:
    if(choice == 1):
        msg = getTextFromUser()
        enc = encryption.encrypt(key, msg)
        storeEncryption(enc)
    elif(choice == 2):
        printOutFile(key)
    else:
        raise Exception("Value returned from userChoice was not a valid option in program function")

def init() -> str:
    key = None
    with open('text.txt', 'r') as file:
        key = file.readline().rstrip()

    if key == '':
        key = encryption.createKey()
        storeEncryption(key)

    return key



def program() -> None:
    key = init()

    choice = getUserChoice()
    handleChoice(key, choice)




if __name__ == '__main__':
    program()