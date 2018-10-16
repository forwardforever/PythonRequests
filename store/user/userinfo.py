#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:forever
# date 2018/10/16 15:25 
import requests
from store.api import url
from store.user import login
class UserInfoControl(object):
    #初始化对象的方法
    def __init__(self):
        self.URL = url.URL()
        self.userinfo = self.URL.base_online_url +self.URL.userinfo
        self.login = login.LoginControl()
    #获取用户信息的网络请求
    def getUserinfo_Success(self):
        self.login.login_Success()
        self.uid = self.login.getUid()
        self.token = self.login.getToken()
        data={'uid':self.uid,
              'token':self.token}
        self.response=requests.post(url=self.userinfo,data=data).json()
        return  self.response
   #解析数据得到data
    def getData(self):
        self.data =self.response['data']
        return self.data

    def getIcon(self):
        self.icon=self.getData()['icon']
        return self.icon
