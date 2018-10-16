#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:forever
# date 2018/10/16 14:56 
from store.api import url
from store.user import login
import requests
class UploadPicControl(object):
    #初始化对象
    def __init__(self):
        self.URL = url.URL()
        self.uploadpic=self.URL.base_online_url+self.URL.upload_pic
        self.login=login.LoginControl()
     #上传头像网络请求
    def uploadpic_Success(self):
       self.login.login_Success()
       self.uid= self.login.getUid()
       data={'uid':self.uid}
       files ={'file':('h.png',open('E:/h.png','rb'),'image/png')}
       self.response= requests.post(url=self.uploadpic,data=data,files=files).json()
       return  self.response





