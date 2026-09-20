def get_number(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Enter number only.")

def match(data, search):
    info = []
    search = search.split()

    for searches in search:
        for a in data:
            if searches.lower() in a.lower():  
                info.append(a)
    info = set(info)
    return info    