import os

file_name = "database.txt"
separator = "=========================="

def Search(filename, searchBy, searchKey):
    found = False
    with open(file_name, "r") as file:
        database = file.read().strip()
        records = database.split("\n\n")

        for line in records:
            data = line.strip().split("\n")
             # ID
            if searchBy == '1':
                if int(data[0]) == searchKey:
                    print(separator)
                    print(f"ID: {data[0]}")
                    print(f"Name: {data[1]}")
                    found = True
             # Name
            elif searchBy == '2':
                if searchKey.lower() in data[1].lower():
                    print(separator)
                    print(f"ID: {data[0]}")
                    print(f"Name: {data[1]}")
                    found = True
                    
    if not found:
        print("Record does not exist.")

def Add():
    pass

def Edit():
    pass

def Delete():
    pass

def main():
    if not os.path.exists(file_name):
        open(file_name, "w").close()

    while True:
        print("+------------------------+")
        print("    [1] Add Record")
        print("    [2] Search Record")
        print("    [3] Update Record")
        print("    [4] Delete Record")
        print("    [5] Exit")
        print("+------------------------+")
        choice = input("Select an option: ")

        match choice:
            case '1':
                pass

            case '2':                
                searchBy = input("Search by: [1] ID or [2] Name: ")
                # ID
                if searchBy == '1':
                    while True:
                        try:
                            searchID = int(input("Enter ID: "))
                            break
                        except: print("Invalid input, try again...")
                    Search(file_name, searchBy, searchID)
                    
                # Name
                elif searchBy == '2':
                    searchName = input("Enter name: ")
                    if searchName == '':
                        print("Name should not be empty...")
                    else:
                        Search(file_name, searchBy, searchName)
                
                else:
                    print("Invalid input, try again...")
                    
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