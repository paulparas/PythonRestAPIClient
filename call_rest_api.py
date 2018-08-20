import requests
r = requests.get('') # Makes r an object conaining information about the request and the response data
print(r.text) # r.text is the raw response
input()