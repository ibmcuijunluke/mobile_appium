from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkrerunner import MonkeyDevice as md
from com.android.monkeyrunner import MonkeyImage as mi

#连接设备
device=mr.waitForConnection()
if not device:
    print("未连接成功，请重新连接")
else:
    print("连接成功……")
#屏幕触发滑动
device.drag(X,Y,"DOWN_AND_UP")
#输入字符串
device.touch(X,Y,"DOWN_AND_UP")
device.type("XXX")
#点击触发
device.touch(X,Y,"DOWN_AND_UP")
#截图及存储操作
result=device.takeSnapshot()
result.writeToFile("E:\\XX\\picture.png","png")
#循环操作
for i in range(1,12):
    print("……")