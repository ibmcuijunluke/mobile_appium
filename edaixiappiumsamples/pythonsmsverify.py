# python ���룬��Ҫͨ��adb log����ȡapk������ȡ�Ķ�����Ϣ��Ȼ����з�����ȿ�ʹ��
# __author__ = 'guozhenhua'
#coding=utf-8
import urllib2
import os,time



#����������֤��
os.system("adb logcat -c")
cmd="adb logcat -d |findstr E/SmsRec"
#time.sleep(30);
while(1):
    smscode= os.popen(cmd).read()
    #print smscode
    if (smscode!=""):
        smscode=smscode.split("��֤�룺")[1].split("��")[0]
        break;
print "��֤����:"+smscode