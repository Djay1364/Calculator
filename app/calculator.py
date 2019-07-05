# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 16:19:59 2019

@author: tiwar
"""

class CalcMachine(object):
    def div(self,a,b):
        if isinstance(a, int) and isinstance(b, int):
            return a/b
        else:
            raise Exception('Invalid Arguments')