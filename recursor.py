#Used to recursively send POST requests to a url with a predefined payload.
import requests

def send_requests(url, keyword, payload):
    for item in payload:
        string = url.replace(keyword, item, 1)
        response = requests.get(string)
        print("Sent request to: " + string + " with status code: " + str(response.status_code))
        #if response.status_code == 200:
        #   print("Text: " + response.text)