#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class dog1:
    """class of dog"""
    def __init__(self,name,age):
        """constructor menthod"""
        self.name = name
        self.age = age
        print("this is constructor")
        print("this will also print")
    def sit(self):
        """sit method"""
        print(f"{self.name} is dog")
    def roll(self):
        """roll method"""
        print(f"{self.age} is age of dog")

