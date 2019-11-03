# coding: utf-8
import os

def ts():
    try:
        print 5/0
        pass
    except ZeroDivisionError:
        print "failed"
        pass

ts()