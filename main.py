import function, file_handling

data = []
search_history = []

try:
    file_handling.load_data(data)
    file_handling.load_history(search_history)
    print(f"Documents loaded: {len(data)}")
    print(f"History loaded: {len(search_history)}")
        
    choice = 0
    while choice != 6:

        choice = function.menu()

        if choice == 1:
            search = function.search(data)
            
            if search is not None:
                search_history.append(search)
                file_handling.save_history(search_history)

        elif choice == 2:
            function.view_data(data)

        elif choice == 3:
            function.add_data(data)
            file_handling.save_data(data)

        elif choice == 4:
            function.history(search_history)

        elif choice == 5:
            function.total_searches(search_history)
            function.recent_search(search_history)
            function.most_search(search_history)

        elif choice == 6:
            function.exit_program()

        else:
            function.invalid()

except:
    print("Write a information to start program.")
    function.add_data(data)
    file_handling.save_data(data)
    function.search(data)
    file_handling.save_history(search_history)