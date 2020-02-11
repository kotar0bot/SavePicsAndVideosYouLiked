import json, config
from requests_oauthlib import OAuth1Session
import re

CONSUMER_KEY = config.CONSUMER_KEY
CONSUMER_SECRET = config.CONSUMER_SECRET
ACCESS_TOKEN = config.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = config.ACCESS_TOKEN_SECRET

USER_ID = config.USER_ID

twitter = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

url = "https://api.twitter.com/1.1/favorites/list.json"

params ={'screen_name' : USER_ID, 'count' : 2}
res = twitter.get(url, params = params)

def main():
    if res.status_code == 200:
        for line in json.loads(res.text):
            for i in line['extended_entities']['media']:
                if('video_info' in i): #if the tweet contains a video.
                    dic = {}
                    for v in i['video_info']['variants']:
                        if ('.mp4' in v['url']): #only .mp4 file.
                            dic[v['url']] = find_max_size(v['url'])
                    print(max(dic, key=dic.get).encode('cp932', 'ignore').decode('cp932'))
                else:
                    # print((line['user']['name'] + '::' + line['text']).encode('cp932', 'ignore').decode('cp932'))
                    print((i['media_url_https']).encode('cp932', 'ignore').decode('cp932'))
            # print(line['created_at'])
            # print('*******************************************')
    else:
        print("Failed: %d" % res.status_code)

def find_max_size(url): #Find the max size video.
    s = re.findall(r'/\d+x\d+/', url) #e.g. /720x1280/
    t = re.findall(r'/\d+x', str(s[0])) #e.g. /720x
    u = re.findall(r'x\d+/', str(s[0])) #e.g. x1280/
    x = int(t[0].replace('x', '').replace('/', '')) #e.g. 720
    y = int(u[0].replace('x', '').replace('/', '')) #e.g. 1280
    return x * y

main()