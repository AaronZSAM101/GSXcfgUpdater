# GSXcfgUpdater
## 用途
用于GSX每次更新后，写入客制化涂装以及对应读取代码的脚本。

**别问这两个脚本为什么存在，问就是FSDT一直不更新，邮件发了好几封了都当没看见，只能出此下策**

**哪天FSDT看到了更新上去了这两个脚本就没有存在的意义了**

## 使用说明
### 先决条件
**1.请在运行前安装好Python，Python可以通过以下两种（最方便的）途径安装：**
- **点击[此链接](https://www.python.org/)，在网站的Download部分找到Python并安装**
- **在微软商店（Microsoft Store）中搜索Python直接安装**

**2.请在运行以下脚本前准备好以下路径:**
- **你的GSX安装路径(也就是Addon Manager文件夹所在的位置)**
- **客制化涂装包位置(涂装包内的文件夹层级应和Addon Manager\texture目录下的文件夹层级一样)**
### 使用教程
- 如果你是首次安装:
    - ~~使用powershell运行 ```ForInitialInstall.py```（按Win+S，输入powershell，再输入python+空格+脚本文件所在路径。例：```python C:\Mengqiu\Desktop\ForInitialInstall.py```，再按提示输入路径。（为确保不出错，请**复制粘贴**路径，否则报错）~~
    **[2023.09.24 更新]** 由于shutil copytree函数不支持覆盖已有目录的文件，然后我又不想修，故建议**直接将texture文件夹的三个文件夹（`catering` `handling` `jetwaylogo`）直接复制到 `Addon Manager\texture`中并覆盖**
    - ~~若运行成功，脚本会提示：`Mission Complete`，反之则会报错（脚本已经过测试，理论上应该不会再出错）。~~
    **[2023.09.24 更新] 覆盖完成后，运行`ForFutherUpdate.py`**
- 如果你刚更新完GSX：
    - 使用powershell运行 `ForFutherUpdate.py`（按Win+S，输入powershell，再输入python+空格+脚本文件所在路径。例：`python C:\Mengqiu\Desktop\ForFutherUpdate.py`，再按提示输入路径。（为确保不出错，请**复制粘贴**路径，否则报错）
    - 若运行成功，脚本会提示：`Mission Complete`，反之则会报错（脚本已经过测试，理论上应该不会再出错）。
