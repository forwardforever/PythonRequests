#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:forever
# date 2018/10/16 11:00 
import unittest
from store.user import login
class LoginUnit(unittest.TestCase):
    #单元测试的初始化方法
    @classmethod
    def setUpClass(cls):
      cls.login=  login.LoginControl()



    def test_Login(self):
      self.response=  self.login.login_Success()
      print self.response

      self.uid= self.login.getUid()

      self.assertEqual("21387",str(self.uid))
