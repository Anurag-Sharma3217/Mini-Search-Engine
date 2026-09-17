import function

data = []
search_history = []

function.load_data(data)
function.load_history(search_history)

choice = 0
while choice != 5:

    choice = function.menu()

    if choice == 1:
        search = function.search(data)
        if search is not None:
            search_history.append(search)
            function.save_history(search_history)

    elif choice == 2:
        function.view_data(data)

    elif choice == 3:
        function.add_data(data)
        function.save_data(data)

    elif choice == 4:
        function.history(search_history)

    elif choice == 5:
        function.exit_program()

    else:
        function.invalid()
