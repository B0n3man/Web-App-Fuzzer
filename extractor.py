#Used to extract data from a file and return it as a list

def extract_data(path):
    payload = []
    with open(path, 'r') as file:
        for line in file:
            payload.append(line.strip())
        return payload