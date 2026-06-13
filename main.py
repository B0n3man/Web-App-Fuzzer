#Will be used to import all other functions and run the program.
from extractor import extract_data
from recursor import send_requests

print("Welcome to the Web App Fuzzer!")
print("Enter the URL you want to fuzz:") #URL input by the user to fuzz
url = input()

print("Enter the keyword you want to fuzz:") #Keyword in the url that will be replaced by the payloads from the file
keyword = input()

print("Enter the path to payload file:") #The path to payload file given by the user (temporary)
path = input()

def get_payload(): #function to get the individual payloads from the file and return them as a list
    payload = extract_data(path)
    return payload

send_requests(url, keyword, get_payload()) #function to send the requests to the url

if __name__ == "__main__":
    get_payload()