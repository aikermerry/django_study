from django.test import TestCase

# Create your tests here.
# -*- coding:utf-8 -*-
class Solution:
    # array 二维列表
    def Find(self, target, array):
        # write code here
        list_len=len(array)//2

        if target[list_len-1][1]<target:
            self.Find(target,array[:list_len])
        if target[list_len][0]>target:
            self.Find(target,array[list_len:])
        if list_len == 0:
           if target[0][1]==target or target[0][0]==target:
               return 1
           return 0
