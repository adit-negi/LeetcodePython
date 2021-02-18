import requests
import json
a = requests.get('https://jsonmock.hackerrank.com/api/articles?page=1')
response = json.loads(a.content.decode('utf-8'))
