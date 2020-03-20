from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from pathlib import Path
import config

def upload_pics_videos():
  gauth = GoogleAuth()
  gauth.CommandLineAuth()
  drive = GoogleDrive(gauth)

  for p in Path("pics").glob("*"):
    q = str(p)
    f = drive.CreateFile({
      "parents": [{
        "id": config.GOOGLEDRIVE_PICS_DIRECTORY_ID
        }]
      })
    f.SetContentFile(q)
    f.Upload()
    print("画像アップロード: {0} {1}".format(f['title'], f['id']).encode('cp932', 'ignore').decode('cp932'))

  for p in Path("videos").glob("*"):
    q = str(p)
    f = drive.CreateFile({
      "parents": [{
        "id": config.GOOGLEDRIVE_VIDEOS_DIRECTORY_ID
        }]
      })
    f.SetContentFile(q)
    f.Upload()
    print("動画アップロード: {0} {1}".format(f['title'], f['id']).encode('cp932', 'ignore').decode('cp932'))