import requests

# reference: http://dart.fss.or.kr/dsap001/guide.do

URL = 'http://dart.fss.or.kr/api/search.json'
params = {'auth': 'YOUR_API_KEY', 'page_set': 100}
res = requests.get(URL, params=params)

print('status code: ' + str(res.status_code))
print('json: ' + str(res.json()))

