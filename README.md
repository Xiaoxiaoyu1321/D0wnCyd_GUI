# D0wnCyd GUI

### 这是一个什么软件    
这是一个可以让你在任意支持完整Python的计算机上下载Cydia源上软件包的软件，这是带有GUI 的版本，所以请确保您使用的 Windows、macOS 或 Linux，我们只测试过在这三个系统上能够正确运行，欢迎您开拓更多的操作系统支持。     

### 如何开始下载   
如果你打算开始下载一个或多个deb 文件，请确保您已经准备好了以下内容：  

1. 您要爬取的Cydia 源地址及其信息    
2. 您要模拟爬取的iPhone 的型号、固件版本的具体信息（如您需要知道： iPhone 4，iOS 7.1.2）   

如果您已经准备好这些信息，那么你可以开始前往 *Release* 页面下载最新版本的客户端   

请您通过 pip install 指令，依次安装以下支持库：   

```
wxpython
subprocess
```

这是必要的库，请您务必要安装，这是安装命令的示例：  
```
适用于 Windows

pip install wxpython
pip install subprocess

适用于 macOS、Linux（可能）

pip3 install wxpython
pip3 install subprocess
```

**请注意，安装命令只是示例，如果您在不同的操作系统或在不同的环境下，命令的使用和库的安装可能会不同，请您查找相关文档，以了解您操作系统的pip如何使用**


在您安装好一切支持库后，您可以在软件目录，打开命令提示符(Windows) 或 终端(macOS、Linux) ，输入以下指令：  

```
适用于Windows

python main.py

适用于 macOS、Linux

python3 main.py

```

**请注意，如果您使用macOS或 Linux，您可能需要在软件内部的"Python命令"输入框中，将"Python"改为"Python3"，以确保程序正确调用Python**


## Python 注意事项

本程序默认调用系统Python，请确保您系统的Python3已经正确安装并配置环境变量，否则将无法使用软件    
