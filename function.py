import utils

def menu():
    print('''\n==============================
      MINI SEARCH ENGINE
==============================

1. Search
2. View Documents
3. Add Document
4. View Search History
5. Exit

Enter choice: \n''')

    return utils.get_number("")

def search(data):

    if data:
        searchs = input()

        if searchs.strip() is not "":
            info = utils.match(data, searchs)

            if info:
                print(f"\n{len(info)} results found.")
                for i, infos in enumerate(info, start=1):                  
                    print(f"{i}. {infos}")

            else:
                print("No results found.")

            return searchs

        else:
            print("Search cannot be empty.")    

    else:
        print("Data inavaiable.")

def view_data(data):

    if data:
        for i, info in enumerate(data, start=1):
            print(i, info)

    else:
        print("Data inavaiable.")

def add_data(data):
    info = input("Enter data: ")
    data.append(info)
    print("Data saved.")

def history(history):
    for i, h in enumerate(history, start=1):
        print(f"{i}. {h}")

def exit_program():
    print("Thank you for using.")

def invalid():
    print("Invalid option.")

#File Handling's functions to make the programs more useful and real.

def save_data(data):
    file = open("documents.txt", "w")
    for info in data:
        file.write(info + "\n")
    file.close()

def load_data(data):
    file = open("documents.txt", "r")
    for line in file:
        line = line.strip("\n")
        data.append(line)
    file.close()

def save_history(history):
    file = open("historyfile.txt", "w")
    for searches in history:
        file.write(searches + "\n")
    file.close()

def load_history(history):
    file = open("historyfile.txt", "r")
    for line in file:
        line = line.strip("\n")
        history.append(line)
    file.close()