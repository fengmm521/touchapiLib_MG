#!/usr/bin/env python
# -*- coding: utf-8 -*-
#本代码来自所出售产品的淘宝店店主编写
#未经受权不得复制转发
#淘宝店：https://fengmm521.taobao.com/
#再次感谢你购买本店产品
import os,sys
import time
import touchutil as tapi


from sys import version_info  


isTest = False

#获取当前python版本
def pythonVersion():
    return version_info.major


def readcom(t):
    n = t.inWaiting()
    while n<=0:
        time.sleep(0.01)
        n = t.inWaiting()
    pstr = t.read(n)
    if pythonVersion() > 2:
        print(pstr.decode())
    else:
        print(pstr)
    return pstr
    

def sendcmd(t,cmd):
    sendstr = cmd
    if cmd[-1] != '\r':
        if type(sendstr) != str:
            sendstr = sendstr.decode() + '\r'
            print(sendstr)
        else:
            sendstr +=  '\r'
    if pythonVersion() > 2:
        s = t.write(sendstr.encode())
    else:
        s = t.write(sendstr.encode())
    t.flush()

def sendAndread(t,v):
    if isTest:
        f = open('test.txt','a')
        f.write(v + '\n')
        f.close()
    else:
        sendcmd(t,v)
        time.sleep(0.03)
        return readcom(t)


_configobj = tapi._configobj
    
def setSpeed(pSpeed):
    if pSpeed > 12000:
        print('ERRO,set speed is to fast!')
        return False
    elif pSpeed > 0 and pSpeed <= 12000:
        _configobj.setSpeed(pSpeed)
    return True
#设置置串口波特率和串口号
def configSerial(port,btv=9600):
    _configobj.configSerial(port,btv)

#打开串口
def openSerial(port = None,btv = 9600):
    if not port:
        return _configobj.openSerial()
    else:
        _configobj.configSerial(port,btv)
        return _configobj.openSerial()
#关闭串口
def closeSerial():
    _configobj.closeSerial()

#获取串口接口
def getSerial():
    return _configobj.getSerial()

#移动到绝对坐标xy
def moveTo(x,y):
    cmds = []
    cmds.append(tapi.conventCMD('ac'))
    tmpstr = 'X'+str(x)+'Y'+str(y)
    cmds.append(tapi.conventCMD(tmpstr))
    for i,v in enumerate(cmds):
        if v:
            sendAndread(_configobj.t, v)
        else:
            print('cmd erro:' + v)

#移动到相对当前位置的相对坐标
def moveBy(x,y):
    cmds = []
    cmds.append(tapi.conventCMD('rc'))
    tmpstr = 'X'+str(x)+'Y'+str(y)
    cmds.append(tapi.conventCMD(tmpstr))
    for i,v in enumerate(cmds):
        if v:
            sendAndread(_configobj.t, v)
        else:
            print('cmd erro:' + v)

#设置点击头按下时电机角度
def setTouchDoneValue(v):
    _configobj.tDoneValue = v

def setTouchUpValue(v):
    _configobj.tUpValue = v

def touchDone(p = 'noValue'):
    if p == 'noValue':
        tmpstr = 's' + str(_configobj.tDoneValue)
        cmd = tapi.conventCMD(tmpstr)
        sendAndread(_configobj.t, cmd)
    else:
        tmpstr = 's' + str(p)
        cmd = tapi.conventCMD(tmpstr)
        sendAndread(_configobj.t, cmd)

def touchUp(p = 'noValue'):
    if p == 'noValue':
        tmpstr = 's' + str(_configobj.tUpValue)
        cmd = tapi.conventCMD(tmpstr)
        sendAndread(_configobj.t, cmd)
    else:
        tmpstr = 's' + str(p)
        cmd = tapi.conventCMD(tmpstr)
        sendAndread(_configobj.t, cmd)

def test():
    if os.path.exists('test.txt'):
        os.remove('test.txt')
    dev = '/dev/cu.usbmodem141101' 
    btv = 9600
    print('port:',dev)
    print('btv:',btv)
    t = openSerial(dev,btv)
    if t:
        print(t.name)               #串口名
        print(t.port)               #串口号
        print(t.baudrate)           #波特率
        print(t.bytesize)           #字节大小
        print(t.parity)             #校验位N－无校验，E－偶校验，O－奇校验
        print(t.stopbits)           #停止位
        print(t.timeout)            #读超时设置
        print(t.writeTimeout)       #写超时
        print(t.xonxoff)            #软件流控
        print(t.rtscts)             #硬件流控
        print(t.dsrdtr)             #硬件流控
        print(t.interCharTimeout)   #字符间隔超时
        print('-'*10)
        time.sleep(5)
        readcom(t)

        while True:
            time.sleep(1)
            moveTo(10, 10)
            time.sleep(1)
            moveTo(0, 0)
            
        t.close()
    else:
        print('串口不存在')

if __name__ == '__main__':
    print('Thanks for using!')
    print('https://fengmm521.taobao.com/')
    test()