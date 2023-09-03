import requests
import sys
import os
from tqdm import tqdm
version="20230073101"
#'Telesphoreo APT-HTTP/1.0.592'
server = "127.0.0.1"
abc = "LF"
path = "Packages"

try:
    server=sys.argv[1] #服务器地址
    path = sys.argv[2] #目录
    server_min = sys.argv[3]
    iPhone_Machine = sys.argv[4]
    iPhone_Fireware = sys.argv[5]
    UID = sys.argv[6]
    UA = sys.argv[7]
    
    
    
    print("下载地址：",server)
    print("保存到：" + path)
    print("请求域名：" ,server_min)
    print("iPhone型号:" + iPhone_Machine)
    print("iPhone固件：" + iPhone_Fireware)
    print("UID:" + UID)
    print("UA:" + UA)
    
    
    
    
    
    
    
    
    if server == "version":
        print(version)
        exit()
        
    print("服务器:" + server)
    print("目录：" + path)
except Exception as q:
    print("遇到错误:" + str(q))

header = {'Host': server_min,
          'X-Machine' : iPhone_Machine ,
          'X-Unique-ID':UID,
          'Connection':'keep-alive',
          'X-Fireware':iPhone_Fireware,
          'Cache-Control':'max-age=0',
          'User-Agent': UA
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

try:
    print("正在下载")
    download(server,path)
    
    
    

except Exception as w:
    print("遇到错误:" , w)