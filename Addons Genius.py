from tkinter import *
import os
# 实例对象
root=Tk()
root.title("Addon Genius")
root.geometry("1420x580+500+500")
label=Label(root)
def btnc():
    btncmd = os.system("color 0A")
    btncmd = os.system("start 1.cmd")
    print(btncmd)
def btn2c():
    btn2cmd = os.system("color 0A")
    btn2cmd = os.system("start 2.cmd")
    print(btn2cmd)
def btn3c():
    btn3cmd = os.system("color 0A")
    btn3cmd = os.system("start 3.cmd")
    print(btn3cmd)
def btn4c():
    btn4cmd = os.system("color 0A")
    btn4cmd = os.system("start 4.cmd")
    print(btn4cmd)
messageline = Label(root,text="\n\n")
message = Label(root, text="请注意！！！部分插件封装不支持自动安装脚本，需要你手动安装。点击“其他插件”可以安装其余的插件")
message2 = Label(root, text="使用前建议关闭UAC,否则你的电脑可能会被UAC弹窗刷屏")
messageline.pack()
message.pack()
message2.pack()
btn=Button(root,text="安装VST3",command=btnc,width=30)
btn2=Button(root,text="安装VST2",command=btn2c,width=30)
btn3=Button(root,text="安装AAX",command=btn3c,width=30)
btn4=Button(root,text="其他插件",command=btn4c,width=30)
btnCls=Button(root,text="退出",command=root.destroy,width=30)
# 控件显示
label.pack(side=TOP)
btn.pack()
btn2.pack()
btn3.pack()
btn4.pack()
btnCls.pack()
# 窗体暂停
root.mainloop()