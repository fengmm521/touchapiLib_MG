#!/usr/bin/python
# -*- coding: utf-8 -*-
#创建SocketServerTCP服务器：
from threading import Thread
import asyncio

import time
import socketserver
# from SocketServer import StreamRequestHandler

import os
import socket

import touchapi
import json


host = '127.0.0.1'
port = 9100
addr = (host,port)

t = None

def configPort(sport = None,sbtv = None,ip = None,netport = None):
    global addr
    global t
    if sport and sbtv and ip and netport:
        addr = (ip,netport)
        t = touchapi.openSerial(sport,sbtv)
    else:
        if os.path.exists('config.json'):
            f= open('config.json','r')
            jstr = f.read()
            f.close()
            print(jstr)
            jobj = json.loads(jstr)
            addr = (jobj['ip'],jobj['netPort'])
            t = touchapi.openSerial(jobj['sport'],jobj['btv'])
        else:
            print('please set serial and server config')
            return False
    return True

class Servers(socketserver.BaseRequestHandler):
    def handle(self):
        print('got connection from ',self.client_address)
        while True:
            try:  
                data = self.request.recv(1024)
            except EOFError:  
                print('接收客户端错误，客户端已断开连接,错误码:')
                print(EOFError )
                break
            except:  
                print('接收客户端错误，客户端已断开连接')
                break
            if not data: 
                break
            print("RECV from ", self.client_address)
            print("recv data:%s"%(data))
            rcvstr = touchapi.sendAndread(t, data)
            if rcvstr:
                self.request.send(rcvstr)

def startServer(sport = None,sbtv = 9600,ip='127.0.0.1',netport=9100):
    cifstate = False
    if sport:
        cifstate = configPort(sport,sbtv,ip,netport)
    else:
        cifstate = configPort()
    if cifstate:
        server = socketserver.ThreadingTCPServer(addr,Servers,bind_and_activate = False)
        server.allow_reuse_address = True   #设置IP地址和端口可以不使用客户端连接等待，并手动绑定服务器地址和端口，手动激活服务器,要不然每一次重启服务器都会出现端口占用的问题
        server.server_bind()
        server.server_activate()
        print('server started:')
        print(addr)
        server.serve_forever()
    
if __name__ == '__main__':
    startServer()