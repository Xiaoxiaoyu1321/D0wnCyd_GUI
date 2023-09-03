import os
import sys
import requests
from tqdm import tqdm
URL = sys.argv[1]
path = sys.argv[2]
URL_min = sys.argv[3]

header = {'Host': URL_min,
          'X-Machine' : "iPhone 3,1" ,
          'X-Unique-ID':'279491f4831444299947a85b7777269766a8ffd6',
          'Connection':'keep-alive',
          'X-Fireware':'7.1.2',
          'Cache-Control':'max-age=0',
          'User-Agent':'Telesphoreo APT-HTTP/1.0.592'
          }

def download(url: str, fname: str):
    # 用流stream的方式获取url的数据
    resp = requests.get(url, stream=True,headers=header)
    # 拿到文件的长度，并把total初始化为0
    total = int(resp.headers.get('content-length', 0))
    # 打开当前目录的fname文件(名字你来传入)
    # 初始化tqdm，传入总数，文件名等数据，接着就是写入，更新等操作了
    with open(fname, 'wb') as file, tqdm(
        desc=fname,
        total=total,
        unit='iB',
        unit_scale=True,
        unit_divisor=1024,
    ) as bar:
        for data in resp.iter_content(chunk_size=1024):
            size = file.write(data)
            bar.update(size)


download(URL,path)