import requests

r = requests.get('https://ipinfo.io').text

print(r)
