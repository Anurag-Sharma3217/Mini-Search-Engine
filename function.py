import utils

def menu():
    print('''\n==============================
      MINI SEARCH ENGINE
==============================

1. Search
2. View Documents
3. Add Document
4. View Search History
5. Search Analytics
6. Exit

Enter choice: \n''')

    return utils.get_number("")

def search(data):

    if data:
        searches = input("Write keywords to search: ")

        if searches.strip() != "":
            info = utils.match(data, searches)

            if info:
                print("\n==========RESULTS==========")                 
                for i, infos in enumerate(info, start=1): 
                    print(f"{i}. {infos}")
                print(f"\nTotal results: {len(info)}")

            else:
                print("No results found.")

            return searches

        else:
            print("Search cannot be empty.")    

    else:
        print("Add documents to start searching.")

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

    if history:
        for i, h in enumerate(history, start=1):
            print(f"{i}. {h}")

    else:
        print("Search something to create historoy.")

def exit_program():
    print("Thank you for using.")

def invalid():
    print("Invalid option.")

# Search Analytics Function

def total_searches(search_history):
    print(f"Total searches: {len(search_history)}")

def recent_search(search_history):
    print(f"most recent searches: {search_history[-1]}")

def most_search(search_history):
    highest_number = 0
    highest_search = ""
    for search in search_history:
        if highest_number < search_history.count(search):
            highest_number = search_history.count(search)
            highest_search = search
    print(f"Most search: {highest_search}")