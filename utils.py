def get_number(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Enter number only.")

def match(data, search):
    info = []
    for a in data:
        if search.lower() in a.lower():
            info.append(a)
    return info       