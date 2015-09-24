# python 代码，主要通过adb log来获取apk包所截取的短信信息，然后进行分析后既可使用
# __author__ = 'guozhenhua'
#coding=utf-8
import urllib2
import os,time



#解析短信验证码
os.system("adb logcat -c")
cmd="adb logcat -d |findstr E/SmsRec"
#time.sleep(30);
while(1):
    smscode= os.popen(cmd).read()
    #print smscode
    if (smscode!=""):
        smscode=smscode.split("验证码：")[1].split("，")[0]
        break;
print "验证码是:"+smscode