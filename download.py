import requests
import datetime
import os

def download_pics(url):
  os.makedirs('pics/', exist_ok=True)
  file_name = "pics/" + datetime.datetime.now().strftime("%Y%m%d%H%M%S%f") + ".jpg"

  response = requests.get(url)
  image = response.content

  with open(file_name, "wb") as stream:
      stream.write(image)

def download_videos(url):
  os.makedirs('videos/', exist_ok=True)
  file_name = "videos/" + datetime.datetime.now().strftime("%Y%m%d%H%M%S%f") + ".mp4"

  response = requests.get(url)
  video = response.content

  with open(file_name, "wb") as stream:
      stream.write(video)
