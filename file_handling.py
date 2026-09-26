#File Handling's functions to make the programs more useful and real.

def save(data, name):
    file = open(name, "w")
    for info in data:
        file.write(info + "\n")
    file.close()

def load(data, name):
    file = open(name, "r")
    for line in file:
        line = line.strip("\n")
        data.append(line)
    file.close()