import os
import sys

try:
    path = sys.argv[1] #源文件地址
    savepath = ".\\list\\"
except Exception as q:
    print(q)


with open(path,'r',encoding="utf-8",newline="\n") as f:
    abc = f.read()
print('q')
if 1 == 1 :
    qaq = abc.split('\n')
    time = 0
    saveabc = ""
    while time < len(qaq):
        chosen = qaq[time]
        cache = chosen.split(":")
        if cache[0] == "Name":
            name = cache[1]
            saveabc = saveabc + "name:"+ cache[1] + "\n"
        elif cache[0] == "Filename":
            saveabc = saveabc + "filename:" + cache[1] + "\n"
        elif cache[0] == "":
            with open(savepath +  name ,'a' ,encoding="utf-8",newline="\n") as f:
                f.write(saveabc)
            saveabc = ""

        time = time + 1

#except Exception as q:
#    print(q)