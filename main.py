import os

file_name = "database.txt"
separator = "=========================="

def Search(fileName, searchBy, searchKey):
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

def Add(name):
    records = []
    with open(file_name, "r") as file:
        lines = file.readlines()
        for i in lines:
            records.append(i.strip())

    latest_id = 0

    for i in range(len(records) - 2):
        if records[i] == separator:
            if int(records[i + 1]) > latest_id:
                latest_id = int(records[i + 1])

    latest_id += 1

    with open(file_name, "a") as file:
        file.write(separator + "\n")
        file.write(f"{latest_id:04d}\n")
        file.write(name + "\n")
        

def Update():
    print(separator)
    try:
        updateID =  int(input("Enter ID of record to update: "))
    except:
        print("Invalid Input!")
        return

    with open(file_name, "r") as file:
        database = file.read().strip()
        if not database:
            print("No Records Found")
            return
        records = database.split("\n\n")

    found = False
    updated_records = []

    for record in records:
        data = record.strip().split("\n")
        if int(data[0]) == updateID:
            print(f"Current Name: {data[1]}")
            new_name = input("Enter New Name: ").strip()
            if new_name == '':
                new_name = data[1].strip()
            updated_records.append(f"{data[0]}\n{new_name}")
            found = True
        else:
            updated_records.append(record.strip())

    if found:
        with open(file_name, "w") as file:
            file.write("\n\n".join(updated_records))
        print("Recored Update Sucessfully")
    else:
        print("Record does not exit")


def Delete(id):
    records = []
    with open(file_name, "r") as file:
        lines = file.readlines()
        for i in lines:
            records.append(i.strip())

    temp = []
    found = False
    for i in range(len(records) - 2):
        if records[i] == separator:
            if records[i + 1] != id:
                temp.append(separator)
                temp.append(records[i + 1])
                temp.append(records[i + 2])
            else:
                found = True

    with open(file_name, "w") as file:
        for line in temp:
            file.write(line + "\n")

    if found:
        print(f"Record with ID {id} deleted successfully.")
    else:
        print(f"Record with ID {id} not found.")

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
                name = input("Enter Name: ")
                Add(name)
                print(f"{name} successfully added!")

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
                    if searchName.strip() == '':
                        print("Name should not be empty...")
                    else:
                        Search(file_name, searchBy, searchName)

                else:
                    print("Invalid input, try again...")

            case '3':
                Update()
                pass

            case '4':
                delete_id = input("Enter ID: ")
                Delete(delete_id)
            
            case '5':
                print("Goodbye!")
                break

            case _:
                print("Invalid input, try again...")


main()
