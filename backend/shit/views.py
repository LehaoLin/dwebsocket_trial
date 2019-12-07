from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import time
from datetime import date
from datetime import datetime
import random
# Create your views here.

import json
from dwebsocket.decorators import accept_websocket,require_websocket



@accept_websocket
def test_websocket(request):
    if request.is_websocket(): # 如果请求是websocket请求：
        i = 0 # 设置发送至前端的次数
        while True:
            i += 1 # 递增次数 i 
            # 休眠1秒
            time.sleep(1)
            # 设置发送前端的数据
            messages = {
                'time':time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(time.time())),
                'msg': 'send %d times!' % i,
            }
            # 设置发送数据为json格式
            request.websocket.send(json.dumps(messages))




# @accept_websocket
# def test_websocket(request):

#     if request.is_websocket(): # 如果请求是websocket请求：

#         WebSocket = request.websocket

#         i = 0 # 设置发送至前端的次数
#         messages = {}

#         while True:
#             i += 1 # 递增次数 i
#             time.sleep(1) # 休眠1秒

#             # 判断是否通过websocket接收到数据
#             if WebSocket.has_messages():

#                 # 存在Websocket客户端发送过来的消息
#                 try:
#                     client_msg = WebSocket.read().decode()
#                 except:
#                     break
#                 else:
#                     # 设置发送前端的数据
#                     messages = {
#                         'time': time.strftime('%Y.%m.%d %H:%M:%S', time.localtime(time.time())),
#                         'server_msg': 'send %d times!' % i,
#                         'client_msg': client_msg,
#                     }

#             else:
#                 # 设置发送前端的数据
#                 messages = {
#                     'time':time.strftime('%Y.%m.%d %H:%M:%S',time.localtime(time.time())),
#                         'server_msg': 'send %d times!' % i,
#                     }

#             # 设置发送数据为json格式
#             request.websocket.send(json.dumps(messages))



def test_websocket_client(request):
    return render(request,'websocket_client.html')

