import json, config
from requests_oauthlib import OAuth1Session
import re
import download
import upload
import delete

CONSUMER_KEY = config.CONSUMER_KEY
CONSUMER_SECRET = config.CONSUMER_SECRET
ACCESS_TOKEN = config.ACCESS_TOKEN
ACCESS_TOKEN_SECRET = config.ACCESS_TOKEN_SECRET

USER_ID = config.USER_ID
delete.delete_files("pics/")
delete.delete_files("videos/")
twitter = OAuth1Session(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

url = "https://api.twitter.com/1.1/favorites/list.json"

params ={'screen_name' : USER_ID, 'count' : 200}
res = twitter.get(url, params = params)

def main():
    if res.status_code == 200:
        for line in json.loads(res.text):
            if('extended_entities' not in line):
                return
            for i in line['extended_entities']['media']:
                if('video_info' in i): #if the tweet contains a video.
                    dic = {}
                    for v in i['video_info']['variants']:
                        if ('.mp4' in v['url']): #only .mp4 file.
                            dic[v['url']] = find_max_size(v['url'])
                    print("動画ダウンロード: {0}".format(max(dic, key=dic.get)).encode('cp932', 'ignore').decode('cp932'))
                    download.download_videos(max(dic, key=dic.get))
                else:
                    print("画像ダウンロード: {0}".format(i['media_url_https']).encode('cp932', 'ignore').decode('cp932'))
                    download.download_pics(i['media_url_https'])
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
upload.upload_pics_videos()