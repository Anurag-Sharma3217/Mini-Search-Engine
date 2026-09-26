def get_number(message):
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Enter number only.")

def match(data, search):
    results = []
    search = search.split()

    for a in data:
        score = 0
        for searches in search:
            if searches.lower() in a.lower():
                score += 1
        if score > 0:
            results.append((a, score))
    results = set(results)
    results = list(results)
    results.sort(
        key=lambda result: result[1],
        reverse=True
    )
    return results

