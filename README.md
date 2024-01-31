# APIFinder-V1.0.0

该工具目的是为了发现某文件中的路径，然后拼接到某url后，通过响应码及返回长度，快速定位并判断其是否存在未授权。

APIFinder [-h] [-u URL1] [-U URL2] [-i RES]

| 参数 | 描述                                  |      |
| ---- | ------------------------------------- | ---- |
| -u   | 目标url(例如:http://xxx.com/x.js)     |      |
| -U   | 需要拼接的url(例如:http://xxx.com/xx) |      |
| -i   | 输出对应响应码的url及长度(例如:200)   |      |

最终会输出一个result.txt文件，用来存放从目标url提取出来、并拼接上指定url的地址。

![image-20240131101801277](C:\Users\lenovo\AppData\Roaming\Typora\typora-user-images\image-20240131101801277.png)