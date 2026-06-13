#Used to extract data from a file and return it as a list

def extract_data(path):
    payload = [] #defined empty list to store payloads as a list
    with open(path, 'r') as file:
        for line in file: #loop to go through every line in the file and append the payloads to the list
            payload.append(line.strip()) #strip() is used to remove trailing whitespaces
        return payload