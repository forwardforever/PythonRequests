#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:forever
# date 2018/10/16 10:49
from store.api import url
import requests

class LoginControl(object):
    #初始化对象
    def __init__(self):
      self.URL=  url.URL()
      self.login=self.URL.base_online_url+self.URL.login
      #登录的网络请求
    def login_Success(self):
      data={'mobile':"18813605663",
            'password':'123456'}

      self.response=requests.post(url=self.login,data=data).json()

      return self.response

    def getData(self):
      self.data= self.response['data']
      return self.data

    def getUid(self):
       self.uid= self.getData()['uid']
       return self.uid

    def getToken(self):
       self.token= self.getData()['token']
       return self.token



