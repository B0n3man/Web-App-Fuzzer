#Used to recursively send POST requests to a url with a predefined payload.
import requests #importing requests library to send HTTP requests

def send_requests(url, keyword, payload):
    for item in payload: #loop to go through every payload
        string = url.replace(keyword, item, 1) #replace the keyword in the url with the payload
        response = requests.get(string) #send a GET request to the modified url
        print("Sent request to: " + string + " with status code: " + str(response.status_code)) #print the response and status code of the request
        #if response.status_code == 200:
        #   print("Text: " + response.text)