#!/usr/bin/env python
#-*- coding:utf-8 -*-
# author:forever
# date 2018/10/16 15:11 
import unittest
from store.user import uploadpic
class UploadPicUnit(unittest.TestCase):
    #初始化对象
    @classmethod
    def setUpClass(cls):
        cls.uploadpic = uploadpic.UploadPicControl()

    def test_UploadPic(self):
        self.response = self.uploadpic.uploadpic_Success()
        print self.response
