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
    history.clear()
    file = open("historyfile.txt", "r")
    for line in file:
        line = line.strip("\n")
        history.append(line)
    file.close()