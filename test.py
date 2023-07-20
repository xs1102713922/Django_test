import json
import requests

if __name__=='__main__':
    url = 'http://127.0.0.1:8000/test_request'
    headers = {"Content-Type": "application/json"}
    #requests.post(url, headers=headers, data=json)
    print(requests.get(url).text)