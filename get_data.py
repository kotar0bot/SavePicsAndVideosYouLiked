import json, config
from requests_oauthlib import OAuth1Session

CONSUMER_KEY = config.CONSUMER_KEY
CONSUMER_SECRET = config.CONSUMER_SECRET
ACCESS_TOKEN = config.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = config.ACCESS_TOKEN_SECRET

USER_ID = config.USER_ID

twitter = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

url = "https://api.twitter.com/1.1/favorites/list.json"

params ={'screen_name' : USER_ID, 'count' : 5}
res = twitter.get(url, params = params)

if res.status_code == 200:
    for line in json.loads(res.text):
        print((line['user']['name'] + '::' + line['text']).encode('cp932', 'ignore').decode('cp932'))
        print(line['created_at'])
        print('*******************************************')
else:
    print("Failed: %d" % res.status_code)