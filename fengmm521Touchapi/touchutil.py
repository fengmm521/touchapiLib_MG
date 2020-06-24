#!/usr/bin/env python
# -*- coding: utf-8 -*-
#本代码来自所出售产品的淘宝店店主编写
#未经受权不得复制转发
#淘宝店：https://fengmm521.taobao.com/
#再次感谢你购买本店产品
import os,sys
import serial

#指令栈
#运行原理：
#当遇到LS循环开始指令时，新建一个循环栈对象。
#在遇到LE之前，遇到其他指令时，直接入栈
#当遇到LE循环结束指令后，查看剩余循环次数，不为0时减1，同时把运行指针指向栈底
class configObj(object):
    """docstring for MoveSpeedObj"""
    def __init__(self, sp = 9000):
        self.speed = sp
        self.strspeed = 'F'+str(self.speed)
        self.btv = 9600
        self.port = None
        self.t = None  #串口
        self.tDoneValue = 0  #点击头按下时电机转动角度
        self.tUpValue = 30   #点击头抬起时电机转动角度
        print('Thanks for using!')
        print('https://fengmm521.taobao.com/')
    def setSpeed(self,sp):
        self.speed = sp
        self.strspeed = 'F'+str(self.speed)
    def getSpeed(self):
        return self.strspeed
    def setStrSpeed(self,strsp):
        self.speed = int(strsp[1:])
        self.strspeed = strsp
    def setBTV(self,pBTV = 9600):
        self.btv = pBTV
    def setPort(self,pPort):
        self.port = pPort
    def configSerial(self,pPort,pBTV = 9600):
        self.setBTV(pBTV)
        self.setPort(pPort)
    def getBTV(self):
        return self.btv
    def getPort(self):
        return self.port
    def openSerial(self):
        if self.t:
            return self.t
        else:
            if self.port:
                self.t = serial.Serial(self.port,self.btv,timeout=1)
                return self.t
            else:
                print('please set serial port!')
                return None
    def closeSerial(self):
        if self.t:
            self.t.close()
            self.t = None
            print('serial closeed!')
        else:
            print('serial was closed!')
    def getSerial(self):
        if self.t:
            return self.t
        else:
            print('ERRO:serial was not open!')
            return None

_configobj = configObj()
    #转换读取到的命令行
def conventCMD(p):
        cmd = ''
        tmpv = p.replace(' ','').replace('\t','').replace('\r','').replace('\n','').replace('；',';')
        tmpv = tmpv.upper()
        if len(tmpv) > 0:
            if tmpv[0] == 'S':
                xtmpvstr = 'Z' + tmpv[1:]
                cmd = 'A1' + _configobj.getSpeed() + xtmpvstr
            elif tmpv[0] == 'F':
                _configobj.setStrSpeed(tmpv)
                cmd = tmpv
            elif tmpv[0] == 'D':
                # cmds.append('A92' + tmpv[1:] + 'Z0')
                cmd = 'A92' + tmpv[1:] + 'Z0'
            elif tmpv[0] == 'A': #设置移动绝对坐标
                # cmds.append('A90') 
                cmd = 'A90'
            elif tmpv[0] == 'R': #设置移动为相对坐标
                # cmds.append('A91') 
                cmd = 'A91'
            elif tmpv[0] == 'X':
                # cmds.append('A1' + self.speed + tmpv)
                cmd = 'A1' + _configobj.getSpeed() + tmpv
            elif tmpv[0] == 'Y':
                # cmds.append('A1' + self.speed + tmpv)
                cmd = 'A1' + _configobj.getSpeed() + tmpv
                
            elif tmpv[0] == 'Z':
                # cmds.append('A1' + self.speed + tmpv)
                cmd = 'A1' + _configobj.getSpeed() + tmpv
            elif tmpv[0] == 'P':#暂停毫秒数
                # cmds.append("A4" + tmpv)
                cmd = 'A4' + tmpv
            else:
                print('cmds erro with:' + tmpv)
                cmd = None
        else:
            cmd = None
        return cmd

def test():
    pass

if __name__ == '__main__':
    print('Thanks for using!')
    print('https://fengmm521.taobao.com/')
    test()