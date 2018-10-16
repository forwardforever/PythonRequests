#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:forever
# date 2018/10/16 15:46 
import unittest
from store.user import userinfo
class UserInfoUnit(unittest.TestCase):
    #初始化对象的方法
    @classmethod
    def setUpClass(cls):
        cls.userinfo = userinfo.UserInfoControl()

    def test_UserInfo(self):
        self.response =self.userinfo.getUserinfo_Success()
        print self.response

        self.icon=  self.userinfo.getIcon()
        print self.icon
