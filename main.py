import os

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


def program() -> None:
    value = getUserChoice()
    if(value == 1):
        pass
    elif(value == 2):
        pass
    else:
        raise Exception("Value returned from userChoice was not a valid option in program function")



if __name__ == '__main__':
    program()