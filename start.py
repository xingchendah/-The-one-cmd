#做这个是为了更加方便地使用cmd，使不会的小白也会使用cmd
import os #导入os库，以用来运行cmd
import time#增加延时的
print("查看代码请看压缩包的readme.txt")
def guanji(shijian):
    os.system("shutdown -s -t "+str(shijian))
def notguanji():
    os.system("shutdown -a")
#接下来会更新很多。先写核心语句
while True:
    jieguo = input("Administrator>")
    os.system(jieguo)
    if jieguo == "guanji":
        guanji(10000)
    if jieguo == "chongzhi":
        notguanji()
