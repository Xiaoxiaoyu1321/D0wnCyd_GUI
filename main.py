# -*- coding:utf-8 -*-
import wx
import os
import subprocess
import _thread
import sys
#from tkinter import filedialog
PythonPath = ".\\bin\\Python\\python"
PythonPath_version = ".\\bin\\Python\\python --version"
CorePath_version = PythonPath + " " +os.getcwd() +  "\\bin\\Core\\BackVersion.py"
CorePath  = os.getcwd() + "\\bin\\Core\\"
CorePath_DownPkg = CorePath + "DownPkg.py"
CorePath_PrintList = CorePath  + "PrintList.py"
CorePath_GetDownloadLink = CorePath + "GetDownloadLink.py"
CorePath_NormalDownload = CorePath + "NormalDown.py"

def binPythonVersion():
    nb =  os.popen(PythonPath_version)
    res = nb.read()
    abc = ""
    for line in res.splitlines():
        abc = abc + line
    return(abc)

def binCoreVersion():
    nb = os.popen(CorePath_version)
    res = nb.read()
    abc = ""
    for line in res.splitlines():
        abc = abc + line
    return(abc)



class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='D0wnCyd_OpenSource_GUI', size=(778, 491),name='frame',style=541072960)
        self.启动窗口 = wx.Panel(self)
        self.Centre()
        self.标签1 = wx.StaticText(self.启动窗口,size=(276, 29),pos=(11, 9),label='D0wnCyd_OpenSource_GUI',name='staticText',style=2321)
        标签1_字体 = wx.Font(16,74,90,400,False,'微软雅黑',28)
        self.标签1.SetFont(标签1_字体)
        self.标签3 = wx.StaticText(self.启动窗口,size=(72, 17),pos=(12, 48),label='Cydia 源：',name='staticText',style=2321)
        self.源地址 = wx.TextCtrl(self.启动窗口,size=(180, 22),pos=(93, 47),value='',name='text',style=0)
        self.下载按钮 = wx.Button(self.启动窗口,size=(73, 33),pos=(19, 73),label='下载',name='button')
        self.下载按钮.Bind(wx.EVT_BUTTON,self.下载按钮_按钮被单击)
        self.选择列表框1 = wx.ListBox(self.启动窗口,size=(459, 358),pos=(285, 50),name='listBox',choices=[],style=0)
        self.载入文件按钮 = wx.Button(self.启动窗口,size=(80, 32),pos=(106, 72),label='载入文件',name='button')
        self.载入文件按钮.Bind(wx.EVT_BUTTON,self.载入文件按钮_按钮被单击)
        self.标签5 = wx.StaticText(self.启动窗口,size=(63, 17),pos=(286, 27),label='包列表：',name='staticText',style=2321)
        标签5_字体 = wx.Font(11,74,90,400,False,'Microsoft YaHei UI',28)
        self.标签5.SetFont(标签5_字体)
        self.下载选中项按钮 = wx.Button(self.启动窗口,size=(80, 32),pos=(662, 409),label='下载选中项',name='button')
        self.下载选中项按钮.Bind(wx.EVT_BUTTON,self.下载选中项按钮_按钮被单击)
        self.日志输出 = wx.TextCtrl(self.启动窗口,size=(254, 306),pos=(15, 109),value='',name='text',style=1073741872)
        
        self.打印控制台内容("当前bin Python版本：" + binPythonVersion())
        self.打印控制台内容("当前bin Core版本：" + binCoreVersion())

    def 打印控制台内容(self,要打印的内容):
        abc =  self.日志输出.GetValue()
        self.日志输出.SetValue(abc + 要打印的内容 + "\n")
        self.日志输出.ShowPosition(self.日志输出.GetLastPosition())

    
    def startDownload(self,qaqqq):
        qwert = "python " + CorePath_DownPkg + " " + self.源地址.GetValue() + " .\Packages.abc"
        screenData = subprocess.Popen(qwert,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        while True:
            line = screenData.stdout.readline()
            self.打印控制台内容(line.decode('utf-8').strip("b'"))
            if line == b'' or subprocess.Popen.poll(screenData) == 0:
                screenData.stdout.close()
                break
    
    def startLoadConfig(self,qaqq):
        fjfjfj ="python " + CorePath_PrintList
        screenData = subprocess.Popen(fjfjfj,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        while True:
            line = screenData.stdout.readline()
            #self.打印控制台内容(line.decode('gbk').strip("b'"))
            self.选择列表框1.Append(line.decode('gbk').strip("b'"))
            if line == b'' or subprocess.Popen.poll(screenData) == 0:
                screenData.stdout.close()
                break

    def startdownloadfile(self,qaqq):
        fjfjfj ="python " + CorePath_GetDownloadLink+ " " +str(self.chosen)
        self.打印控制台内容(fjfjfj)
        nb =  os.popen(fjfjfj)
        res = nb.read()
        abc = ""
        for line in res.splitlines():
            abc = abc + line

        bcd  = abc.split(" ")
        abc = bcd[1]

        

        self.打印控制台内容(abc)
        fjfjfj ="python " + CorePath_NormalDownload + " " + self.源地址.GetValue() +abc +" .\\" +str(self.chosen) +".deb"
        self.打印控制台内容(fjfjfj)
        screenData = subprocess.Popen(fjfjfj,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        while True:
            line = screenData.stdout.readline()
            self.打印控制台内容(line.decode('gbk').strip("b'"))
            self.选择列表框1.Append(line.decode('gbk').strip("b'"))
            if line == b'' or subprocess.Popen.poll(screenData) == 0:
                screenData.stdout.close()
                break
        


    def 下载按钮_按钮被单击(self,event):
        print('下载按钮,按钮被单击')
        _thread.start_new_thread(self.startDownload,(self,))

        

    def 载入文件按钮_按钮被单击(self,event):
        print('载入文件按钮,按钮被单击')
        _thread.start_new_thread(self.startLoadConfig,(self,))

    def 下载选中项按钮_按钮被单击(self,event):
        print('下载选中项按钮,按钮被单击')
        
        #self.打印控制台内容(str(self.选择列表框1.GetSelection()))
        self.chosen = self.选择列表框1.GetSelection()+1
        self.打印控制台内容(str(self.chosen))

        _thread.start_new_thread(self.startdownloadfile,(self,))
        #self.startdownloadfile(self,)


class myApp(wx.App):
    def  OnInit(self):
        self.frame = Frame()
        self.frame.Show(True)
        return True

if __name__ == '__main__':
    app = myApp()
    app.MainLoop()