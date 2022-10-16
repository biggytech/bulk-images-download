import os
import pprint
import time
import urllib.error
from urllib.request import Request, urlopen
import sys

def download_file(req, dst_path):
    try:
        with urllib.request.urlopen(req) as web_file:
            data = web_file.read()
            with open(dst_path, mode='wb') as local_file:
                local_file.write(data)
    except urllib.error.URLError as e:
        print(e)

def download_file_to_dir(req, url, dist_dir):
    download_file(req, os.path.join(dist_dir, os.path.basename(url)))

# validate args count
if not len(sys.argv) == 6:
  print("Invalid number of arguments")
  sys.exit()

orig_url = sys.argv[1]
extension = sys.argv[2]
dist_dir = sys.argv[3]
from_range = int(sys.argv[4])
to_range = int(sys.argv[5])

print("Downloading...")

for i in range(from_range, to_range+1):
  url = orig_url + str(i) + '.' + extension

  req = Request(
      url=url, 
      headers={'User-Agent': 'Mozilla/5.0'}
  )
  download_file_to_dir(req, url, dist_dir)
  
  print("Downloaded " + url)

print("Finished!")