# coding: utf-8
import os
import sys

class Dog(object):
    def __init__(self, name, age):
        self.name = name 
        self.age = age
    def sit(self):
        print self.name.title() + ' is sitting'
    def update_age(self, age):
        self.age = age
        print 'change age ' + str(self.age) 

class China_dog(Dog):
    def __init__(self, name, age):
        super(China_dog, self).__init__(name, age)
    def sit(self):
        print "china_dog is sitting"

china_dog = China_dog("jack", 24)
# china_dog.sit()