# feel free to change these
def Search():
    pass

def Add():
    pass

def Edit():
    pass

def Delete():
    pass

def main():
    while True:
        print("+------------------------+")
        print("    [1] Add Record")
        print("    [2] Search Record")
        print("    [3] Edit Record")
        print("    [4] Delete Record")
        print("    [5] Exit")
        print("+------------------------+")
        choice = input("Select an option: ")

        match choice:
            case '1':
                pass
            case '2':
                pass
            case '3':
                pass
            case '4':
                pass
            case '5':
                print("Goodbye!")
                break
            case _:
                print("Invalid input, try again...")


main()