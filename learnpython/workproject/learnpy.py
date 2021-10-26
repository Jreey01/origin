#!/usr/bin/python3
# -*-coding:utf-8 -*-
# @Time    :2021/10/26:17:26
# @Author   :ELWIN
# @Email    :nwlhb@163.com
# @File     :learnpy.py
import requests
from selenium import webdriver
# -*-coding:utf-8 -*-
# @Time    :2021/4/14 16:12
# @Author   :ELWIN
# @Email    :nwlhb@163.com
# @File     :class_practise.py


class User:
    def __init__(self, first_name, last_name, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.sex = sex

    def describe_user(self):
        print("{}客户的信息是：性别：{}；年龄：{}；".format(self.last_name+self.first_name, self.sex, self.age))

    def greet_user(self):
        if self.sex == "男":
            print("{}先生你好！".format(self.last_name))
        else:
            print("{}女士你好！".format(self.last_name))


user_1 = User("花花", "李", "19", "女")

user_1.describe_user()
user_1.greet_user()
