from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from pathlib import Path
import config

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
  print(f['title'], f['id'])

for p in Path("videos").glob("*"):
  q = str(p)
  f = drive.CreateFile({
    "parents": [{
      "id": config.GOOGLEDRIVE_VIDEOS_DIRECTORY_ID
      }]
    })
  f.SetContentFile(q)
  f.Upload()
  print(f['title'], f['id'])