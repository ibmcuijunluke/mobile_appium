from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkrerunner import MonkeyDevice as md
from com.android.monkeyrunner import MonkeyImage as mi

#�����豸
device=mr.waitForConnection()
if not device:
    print("δ���ӳɹ�������������")
else:
    print("���ӳɹ�����")
#��Ļ��������
device.drag(X,Y,"DOWN_AND_UP")
#�����ַ���
device.touch(X,Y,"DOWN_AND_UP")
device.type("XXX")
#�������
device.touch(X,Y,"DOWN_AND_UP")
#��ͼ���洢����
result=device.takeSnapshot()
result.writeToFile("E:\\XX\\picture.png","png")
#ѭ������
for i in range(1,12):
    print("����")