import requests
r = requests.get('https://www.sojson.com/open/api/weather/json.shtml?city=广州')
r.json()
