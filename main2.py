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




def binCoreVersion():
    nb = os.popen(CorePath_version)
    res = nb.read()
    abc = ""
    for line in res.splitlines():
        abc = abc + line
    return(abc)







class Frame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title='D0wnCyd_OpenSource_GUI', size=(781, 519),name='frame',style=541072960)
        self.启动窗口 = wx.Panel(self)
        self.Centre()
        self.标签1 = wx.StaticText(self.启动窗口,size=(272, 24),pos=(8, 13),label='请求协议:(http://或https://，默认是http://)',name='staticText',style=17)
        self.请求协议 = wx.TextCtrl(self.启动窗口,size=(73, 25),pos=(7, 41),value='http://',name='请求协议',style=0)
        self.标签2 = wx.StaticText(self.启动窗口,size=(294, 29),pos=(8, 74),label='Cydia源地址（只输入域名，不要添加其他任何文本)',name='staticText',style=17)
        self.源地址 = wx.TextCtrl(self.启动窗口,size=(221, 25),pos=(7, 121),value='',name='源地址',style=0)
        self.标签3 = wx.StaticText(self.启动窗口,size=(246, 24),pos=(7, 97),label='例子：apt.example.com',name='staticText',style=17)
        self.标签4 = wx.StaticText(self.启动窗口,size=(271, 24),pos=(7, 154),label='请求的Packages文件，默认是/Packages.gz',name='staticText',style=17)
        self.请求的文件 = wx.TextCtrl(self.启动窗口,size=(154, 27),pos=(7, 182),value='/Packages.gz',name='请求的文件',style=0)
        self.标签5 = wx.StaticText(self.启动窗口,size=(245, 24),pos=(7, 217),label='请求的User-Agent，不知道的不要修改',name='staticText',style=17)
        self.UA = wx.TextCtrl(self.启动窗口,size=(234, 28),pos=(7, 246),value='Telesphoreo APT-HTTP/1.0.592',name='UA',style=0)
        self.标签6 = wx.StaticText(self.启动窗口,size=(92, 24),pos=(8, 289),label='请求的iPhone ：',name='staticText',style=17)
        self.型号 = wx.TextCtrl(self.启动窗口,size=(87, 25),pos=(185, 306),value='iPhone 3,1',name='text',style=0)
        self.标签7 = wx.StaticText(self.启动窗口,size=(137, 24),pos=(26, 337),label='固件版本(例子：7.1.2)：',name='staticText',style=17)
        self.标签8 = wx.StaticText(self.启动窗口,size=(155, 24),pos=(21, 310),label='型号(例子： iPhone 3,1)：',name='staticText',style=2321)
        self.固件 = wx.TextCtrl(self.启动窗口,size=(87, 27),pos=(185, 333),value='7.1.2',name='text',style=0)
        self.标签9 = wx.StaticText(self.启动窗口,size=(70, 22),pos=(28, 367),label='Unique-ID:',name='staticText',style=17)
        self.标识ID = wx.TextCtrl(self.启动窗口,size=(173, 25),pos=(99, 364),value='',name='标识ID',style=0)
        self.下载Packages = wx.Button(self.启动窗口,size=(263, 27),pos=(12, 392),label='下载Packages',name='button')
        self.下载Packages.Bind(wx.EVT_BUTTON,self.下载Packages_按钮被单击)
        self.编辑框8 = wx.TextCtrl(self.启动窗口,size=(457, 124),pos=(293, 54),value='',name='text',style=1073741856)
        #self.编辑框8.Disable()
        self.标签10 = wx.StaticText(self.启动窗口,size=(80, 24),pos=(293, 27),label='日志：',name='staticText',style=17)
        self.标签11 = wx.StaticText(self.启动窗口,size=(80, 24),pos=(293, 200),label='软件列表：',name='staticText',style=17)
        self.列表框1 = wx.ListBox(self.启动窗口,size=(449, 225),pos=(292, 226),name='listBox',choices=[],style=32)
        self.加载Packages = wx.Button(self.启动窗口,size=(262, 27),pos=(12, 422),label='加载Packages',name='button')
        self.加载Packages.Bind(wx.EVT_BUTTON,self.加载Packages_按钮被单击)
        self.下载deb = wx.Button(self.启动窗口,size=(80, 26),pos=(375, 196),label='下载选中项',name='下载deb')
        self.下载deb.Bind(wx.EVT_BUTTON,self.下载deb_按钮被单击)
        self.标签12 = wx.StaticText(self.启动窗口,size=(100, 24),pos=(384, 25),label='Python 命令：',name='staticText',style=2321)
        self.Python命令 = wx.TextCtrl(self.启动窗口,size=(138, 23),pos=(493, 22),value='python',name='Python命令',style=0)
    def 打印控制台内容(self,要打印的内容):
        abc =  self.编辑框8.GetValue()
        self.编辑框8.SetValue(abc + 要打印的内容 + "\n")
        self.编辑框8.ShowPosition(self.编辑框8.GetLastPosition())
    
    def startDownload(self,qaqqq):
        
        下载地址 = self.请求协议.GetValue() +  self.源地址.GetValue() + self.请求的文件.GetValue()
        保存地址 = ".\Packages.压缩包"
        源地址 = self.源地址.GetValue()
        iPhone型号 = self.型号.GetValue()
        iPhone固件 = self.固件.GetValue() 
        标识ID = self.标识ID.GetValue() 
        请求UAA = self.UA.GetValue()
        空格 = " "
        
        qwert = self.Python命令.GetValue() +  " " + CorePath_DownPkg + 空格 + 下载地址 + 空格 + 保存地址 + 空格 + 源地址 + 空格 + iPhone型号 + 空格 + iPhone固件+ 空格 + 标识ID + 空格 + 请求UAA
        
        
        screenData = subprocess.Popen(qwert,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        while True:
            line = screenData.stdout.readline()
            self.打印控制台内容(line.decode('gbk').strip("b'"))
            if line == b'' or subprocess.Popen.poll(screenData) == 0:
                screenData.stdout.close()
                break
    
        self.打印控制台内容("请使用解压缩软件，打开Packages.压缩包，解压Packages文件到当前目录")
    
    
    
    
    
    
    def startLoadConfig(self,qaqq):
        fjfjfj ="python " + CorePath_PrintList
        screenData = subprocess.Popen(fjfjfj,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        while True:
            line = screenData.stdout.readline()
            #self.打印控制台内容(line.decode('gbk').strip("b'"))
            self.列表框1.Append(line.decode('gbk').strip("b'"))
            if line == b'' or subprocess.Popen.poll(screenData) == 0:
                screenData.stdout.close()
                break
    def 下载Packages_按钮被单击(self,event):
        print('下载Packages,按钮被单击')
        _thread.start_new_thread(self.startDownload,(self,))

    def 加载Packages_按钮被单击(self,event):
        print('加载Packages,按钮被单击')
        _thread.start_new_thread(self.startLoadConfig,(self,))

    def 下载deb_按钮被单击(self,event):
        print('下载deb,按钮被单击')

class myApp(wx.App):
    def  OnInit(self):
        self.frame = Frame()
        self.frame.Show(True)
        return True

if __name__ == '__main__':
    app = myApp()
    app.MainLoop()