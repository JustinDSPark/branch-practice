import requests

def get_response():
    return requests.get("https://www.google.com/').status_code
