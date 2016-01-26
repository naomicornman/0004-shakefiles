import os
import requests
zipurl = 'http://stash.compciv.org/scrapespeare/matty.shakespeare.tar.gz'
resp = requests.get(zipurl)
zipdata = resp.content
zname = os.path.join("tempdata", "matty.shakespeare.tar.gz")
zfile = open(zname, "wb")
zfile.write(zipdata)  # i.e. resp.content
zfile.close()
import shutil
shutil.unpack_archive(zname, extract_dir='tempdata')