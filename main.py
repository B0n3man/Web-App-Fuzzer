#Will be used to import all other functions and run the program.
from extractor import extract_data
from recursor import send_requests

print("Welcome to the Web App Fuzzer!")
print("Enter the URL you want to fuzz:")
url = input()

print("Enter the keyword you want to fuzz:")
keyword = input()

print("Enter the path to payload file:")
path = input()

def get_payload():
    payload = extract_data(path)
    return payload

send_requests(url, keyword, get_payload())

if __name__ == "__main__":
    get_payload()